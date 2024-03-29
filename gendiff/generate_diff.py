import json
import yaml
from yaml.loader import SafeLoader
from gendiff.formatters.stylish_formatter import get_stylish_diff
from gendiff.formatters.plain_formatter import get_plain_diff
from gendiff.formatters.json_formatter import get_json_diff


def generate_diff(file1, file2, format='stylish'):
    file1, file2 = open_files(file1), open_files(file2)
    diff_file = get_diff(file1, file2)
    if format == 'stylish':
        return get_stylish_diff(diff_file)
    elif format == 'plain':
        return get_plain_diff(diff_file)
    elif format == 'json':
        return get_json_diff(diff_file)
    raise Exception('Wrong format.\nReport as plain text, stylish and json')


def open_files(file):
    if file.endswith('json'):
        open_file = open(file)
        return parser(open_file, 'json')
    elif file.endswith('yml') or file.endswith('yaml'):
        open_file = open(file)
        return parser(open_file, 'yml')
    raise Exception('Wrong format.\nInput formats: yaml, json.')


def parser(open_file, format):
    if format == 'yml':
        return yaml.load(open_file, Loader=SafeLoader)
    elif format == 'json':
        return json.load(open_file)


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
