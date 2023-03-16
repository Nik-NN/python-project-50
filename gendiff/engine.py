import json
import yaml
from yaml.loader import SafeLoader


def generate_diff(file1, file2):
    file1, file2 = open_files(file1, file2)
    diff = get_diff(file1, file2)
    result = stylish(diff)
    return result

def open_files(file1, file2):
    if 'json' in file1:
        file_1 = json.load(open(file1))
        file_2 = json.load(open(file2))
    else:
        file_1 = yaml.load(open(file1), Loader=SafeLoader)
        file_2 = yaml.load(open(file2), Loader=SafeLoader)
    return file_1, file_2


def change_boolean(value):
    if value is True:
        value = 'true'
    if value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value


def get_diff(file1, file2, depth=' '):
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    result = []
    for key in keys:
        if key not in file1:
            result.append({'name': key, 'status': 'added', 'value': file2[key], 'depth': depth})
        elif key not in file2:
            result.append({'name': key, 'status': 'deleted', 'value': file1[key], 'depth': depth})
        elif type(file1[key]) is dict and type(file2[key]) is dict:
            result.append({'name': key, 'status': 'parent', 'children': get_diff(file1[key], file2[key], depth+' '), 'depth': depth})
        elif file1[key] == file2[key]:
            result.append({'name': key, 'status': 'unchanged', 'value': file1[key], 'depth': depth})
        elif file1[key] != file2[key]:
            result.append({'name': key, 'status': 'changed', 'value1': file1[key], 'value2': file2[key], 'depth': depth})
    return result


def stylish(diff, replacer=' ', space_count=4, deepth=1):
    result = "{\n"
    indent = replacer * space_count * deepth
    for item in diff:
        if item['status'] == 'parent':
            value = stylish(item['children'], replacer, space_count, deepth + 1)
            result += f"{indent[:-2]}  {item['name']}: {value}\n"
        elif item['status'] == 'unchanged':
            value = stringify(item['value'], indent)
            result += f"{indent[:-2]}  {item['name']}: {value}\n"
        elif item['status'] == 'added':
            value = stringify(item['value'], indent)
            result += f"{indent[:-2]}+ {item['name']}: {value}\n"
        elif item['status'] == 'deleted':
            value = stringify(item['value'], indent)
            result +=  f"{indent[:-2]}- {item['name']}: {value}\n"
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
