import json


def find_new_keys(list_key_file1, list_key_file2):
    new_key = []
    for item in list_key_file2:
        if not (item in list_key_file1):
            new_key.append(item)
    return new_key


def list_to_string(lists):
    result = '{\n'
    for item in lists:
        result += f"{item}\n"
    result += '}'
    return result


def open_files(first_file, second_file):
    f1 = json.load(open(first_file))
    f2 = json.load(open(second_file))
    return f1, f2


def change_boolean(file1):
    file2 = file1.copy()
    for item in file2:
        if file2[item] is False:
            file2[item] = 'false'
        elif file2[item] is True:
            file2[item] = 'true'
        elif file2[item] is None:
            file2[item] = 'null'
    return file2


def generate_diff(file1, file2):
    file1, file2 = open_files(file1, file2)
    file1, file2 = change_boolean(file1), change_boolean(file2)
    result = []
    list({"a": 1, "b": 2}.keys())
    for item in file1:
        if file2.get(item, "no such key") == "no such key":
            result.append(f' - {item}: {file1.get(item)}')
        elif file1.get(item) == file2.get(item):
            result.append(f'   {item}: {file1.get(item)}')
        elif file1.get(item) != file2.get(item):
            result.append(f' - {item}: {file1.get(item)}')
            result.append(f' + {item}: {file2.get(item)}')
    list_key_file1 = list(file1.keys())
    list_key_file2 = list(file2.keys())
    new_key = find_new_keys(list_key_file1, list_key_file2)
    for item in new_key:
        result.append(f' + {item}: {file2.get(item)}')
    result.sort(key=lambda x: x[3])
    result = list_to_string(result)
    return result
