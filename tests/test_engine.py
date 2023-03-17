from gendiff.engine import generate_diff


def tests_generate_diff_stylish():
    file_json1 = 'tests/fixtures/file1_for_test.json'
    file_json2 = 'tests/fixtures/file2_for_test.json'
    file_yml1 = 'tests/fixtures/file1_for_test.yml'
    file_yml2 = 'tests/fixtures/file2_for_test.yml'
    f = open("tests/fixtures/result_for_stylish.txt", "r")
    result = f.read()
    assert generate_diff(file_json1, file_json2) == result
    assert generate_diff(file_yml1, file_yml2) == result
    f.close()


def tests_generate_diff_plain():
    file_json1 = 'tests/fixtures/file1_for_test.json'
    file_json2 = 'tests/fixtures/file2_for_test.json'
    file_yml1 = 'tests/fixtures/file1_for_test.yml'
    file_yml2 = 'tests/fixtures/file2_for_test.yml'
    f = open("tests/fixtures/result_for_plain.txt", "r")
    result = f.read()
    assert generate_diff(file_json1, file_json2, format='plain') == result
    assert generate_diff(file_yml1, file_yml2, format='plain') == result
    f.close()
