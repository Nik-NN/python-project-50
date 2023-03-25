def change_boolean(value):
    if type(value) is dict:
        return '[complex value]'
    elif value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    elif type(value) is str:
        value = f"'{value}'"
    return value


def get_plain_diff(diff):  # noqa: C901
    def inner(diff):
        result = ''
        for item in diff:
            if item['status'] == 'parent':
                value = inner(item['children'])
                result += f"{value}"
            elif item['status'] == 'added':
                path = (item['path'])[:-1]
                value = item['value']
                value = change_boolean(value)
                result += f"Property '{path}' was added with value: {value}\n"
            elif item['status'] == 'deleted':
                path = (item['path'])[:-1]
                result += f"Property '{path}' was removed\n"
            elif item['status'] == 'changed':
                path = (item['path'])[:-1]
                val1 = change_boolean(item['value1'])
                val2 = change_boolean(item['value2'])
                result += f"Property '{path}' was updated. "
                f"From {val1} to {val2}\n"
        return result
    return inner(diff).rstrip()
