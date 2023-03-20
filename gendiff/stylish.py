def get_stylish_diff(diff, replacer=' ', space_count=4, deepth=1):
    result = "{\n"
    indent = replacer * space_count * deepth
    for item in diff:
        if item['status'] == 'parent':
            diff = item['children']
            value = get_stylish_diff(diff, replacer, space_count, deepth + 1)
            result += f"{indent[:-2]}  {item['name']}: {value}\n"
        elif item['status'] == 'unchanged':
            value = stringify(item['value'], indent)
            result += f"{indent[:-2]}  {item['name']}: {value}\n"
        elif item['status'] == 'added':
            value = stringify(item['value'], indent)
            result += f"{indent[:-2]}+ {item['name']}: {value}\n"
        elif item['status'] == 'deleted':
            value = stringify(item['value'], indent)
            result += f"{indent[:-2]}- {item['name']}: {value}\n"
        elif item['status'] == 'changed':
            value1 = stringify(item['value1'], indent)
            result += f"{indent[:-2]}- {item['name']}: {value1}\n"
            value2 = stringify(item['value2'], indent)
            result += f"{indent[:-2]}+ {item['name']}: {value2}\n"
    result += indent[:-4] + '}'
    return result


def stringify(value, indent):
    if type(value) is dict:
        result = "{\n"
        indent += '    '
        for el, val in value.items():
            result += f'{indent}{el}: '
            result += stringify(val, indent) + '\n'
        result += indent[:-4] + '}'
    else:
        result = str(change_boolean(value))
    return result


def change_boolean(value):
    if value is True:
        value = 'true'
    if value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value
