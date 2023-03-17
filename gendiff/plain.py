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

def plain(diff):
    result = get_plain_diff(diff)
    return result[:-1]


def get_plain_diff(diff):
    result = ''
    for item in diff:
        if item['status'] == 'parent':
            value = get_plain_diff(item['children'])
            #value = change_boolean(value)
            result += f"{value}"
        elif item['status'] == 'added':
            path_deep = (item['path'])[1:]
            value = item['value']
            value = change_boolean(value)
            result += f"Property '{path_deep}' was added with value: {value}\n"
        elif item['status'] == 'deleted':
            path_deep = (item['path'])[1:]
            result += f"Property '{path_deep}' was removed\n"
        elif item['status'] == 'changed':
            path_deep = (item['path'])[1:]
            value1 = item['value1']
            value2 = item['value2']
            value1 = change_boolean(value1)
            value2 = change_boolean(value2)
            result += f"Property '{path_deep}' was updated. From {value1} to {value2}\n"
    return result
