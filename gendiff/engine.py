import json
import yaml
from yaml.loader import SafeLoader
from gendiff.stylish import get_stylish_diff
from gendiff.plain import get_palin_diff
from gendiff.get_json import get_json_diff


def generate_diff(file1, file2, format='stylish'):
    file1, file2 = open_files(file1), open_files(file2)
    diff_file = get_diff(file1, file2)
    if format == 'stylish':
        result = get_stylish_diff(diff_file)
    elif format == 'plain':
        result = get_palin_diff(diff_file)
    elif format == 'json':
        result = get_json_diff(diff_file)
    return result


def open_files(file):
    if 'json' in file:
        return json.load(open(file))
    elif 'yml' in file or 'yaml' in file:
        return yaml.load(open(file), Loader=SafeLoader)


def get_diff(file1, file2, path=''):  # noqa: C901
    keys = sorted(set(list(file1.keys()) + list(file2.keys())))
    result = []
    for key in keys:
        if key not in file1:
            result.append({'name': key, 'status': 'added',
                           'value': file2[key], 'path': path + f"{key}."})
        elif key not in file2:
            result.append({'name': key, 'status': 'deleted',
                           'value': file1[key], 'path': path + f"{key}."})
        elif type(file1[key]) is dict and type(file2[key]) is dict:
            child = get_diff(file1[key], file2[key], path + f"{key}.")
            result.append({'name': key, 'status': 'parent',
                           'children': child, 'path': path + f"{key}."})
        elif file1[key] == file2[key]:
            result.append({'name': key, 'status': 'unchanged',
                           'value': file1[key], 'path': path + f"{key}."})
        elif file1[key] != file2[key]:
            val1 = file1[key]
            val2 = file2[key]
            result.append({'name': key, 'status': 'changed', 'value1': val1,
                           'value2': val2, 'path': path + f"{key}."})
    return result
