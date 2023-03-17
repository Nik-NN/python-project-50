import json
import yaml
from yaml.loader import SafeLoader
from gendiff.stylish import stylish
from gendiff.plain import plain


def generate_diff(file1, file2, format='stylish'):
    file1, file2 = open_files(file1, file2)
    diff = get_diff(file1, file2)
    if format == 'stylish':
        result = stylish(diff)
    elif format == 'plain':
        result = plain(diff)
    return result

def open_files(file1, file2):
    if 'json' in file1:
        file_1 = json.load(open(file1))
        file_2 = json.load(open(file2))
    else:
        file_1 = yaml.load(open(file1), Loader=SafeLoader)
        file_2 = yaml.load(open(file2), Loader=SafeLoader)
    return file_1, file_2


def get_diff(file1, file2, path=''):
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    result = []
    for key in keys:
        if key not in file1:
            result.append({'name': key, 'status': 'added', 'value': file2[key], 'path': path+f".{key}"})
        elif key not in file2:
            result.append({'name': key, 'status': 'deleted', 'value': file1[key], 'path': path+f".{key}"})
        elif type(file1[key]) is dict and type(file2[key]) is dict:
            result.append({'name': key, 'status': 'parent', 'children': get_diff(file1[key], file2[key], path+f".{key}"), 'path': path+f".{key}"})
        elif file1[key] == file2[key]:
            result.append({'name': key, 'status': 'unchanged', 'value': file1[key], 'path': path+f".{key}"})
        elif file1[key] != file2[key]:
            result.append({'name': key, 'status': 'changed', 'value1': file1[key], 'value2': file2[key], 'path': path+f".{key}"})
    return result
