from gendiff.engine import find_new_keys, list_to_string, change_boolean, generate_diff, open_files


def tests_find_new_keys():
    list_key_file1 = ['a', 'b', 'c']
    list_key_file2 = ['a', 'bb', 'v']
    assert find_new_keys(list_key_file1, list_key_file2) == ['bb', 'v']
    assert list_key_file1 == ['a', 'b', 'c'] and list_key_file2 == ['a', 'bb', 'v']


def tests_list_to_string():
    lists = ['b', 4, 'a']
    result = result = '{\nb\n4\na\n}'
    result_for_empty = '{\n}'
    assert list_to_string(lists) == result
    assert list_to_string([]) == result_for_empty

   
def tests_change_boolean():
    file1 = {'a': None, 'b': 'None', 4: 44, 'c': False, 'f': True}
    result = {'a': 'null', 'b': 'None', 4: 44, 'c': 'false', "f": 'true'}
    assert change_boolean(file1) == result
    assert file1 == {'a': None, 'b': 'None', 4: 44, 'c': False, 'f': True}


def tests_generate_diff():
    file1 = 'tests/fixtures/file1_for_test.json'
    file2 = 'tests/fixtures/file2_for_test.json'
    f = open("tests/fixtures/result_for_generate_diff.txt", "r")
    result = f.read()
    #result = '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'
    assert generate_diff(file1, file2) == result
    f.close()
