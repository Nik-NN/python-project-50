def change_boolean(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    elif isinstance(value, str):
        value = f"'{value}'"
    return value


def get_plain_diff(diff, deep=0):  # noqa: C901
    result = ''
    for item in diff:
        if item['status'] == 'parent':
            value = get_plain_diff(item['children'], deep + 1)
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
            result += f"Property '{path}' was updated. From {val1} to {val2}\n"
    if deep > 0:
        return result
    else:
        return result.rstrip()
