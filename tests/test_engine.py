from gendiff.engine import generate_diff, change_boolean


def tests_generate_diff():
    file_json1 = 'tests/fixtures/file1_for_test.json'
    file_json2 = 'tests/fixtures/file2_for_test.json'
    file_yml1 = 'tests/fixtures/file1_for_test.yml'
    file_yml2 = 'tests/fixtures/file2_for_test.yml'
    f = open("tests/fixtures/result_for_generate_diff.txt", "r")
    result = f.read()
    assert generate_diff(file_json1, file_json2) == result
    assert generate_diff(file_yml1, file_yml2) == result
    f.close()


def tests_change_boolean():
    value = True
    value2 = False
    value3 = None       
    assert change_boolean(value) == 'true'
    assert change_boolean(value2) == 'false'
    assert change_boolean(value3) == 'null'
