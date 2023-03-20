from gendiff.engine import generate_diff
import json

def tests_generate_diff():
    file_json1 = 'tests/fixtures/file1_for_test.json'
    file_json2 = 'tests/fixtures/file2_for_test.json'
    file_yml1 = 'tests/fixtures/file1_for_test.yml'
    file_yml2 = 'tests/fixtures/file2_for_test.yml'
    result_for_stylish = open("tests/fixtures/result_for_stylish.txt", "r").read()
    result_for_plain = open("tests/fixtures/result_for_plain.txt", "r").read()
    result_for_json = open("tests/fixtures/result_for_json.txt", "r").read()
    assert generate_diff(file_json1, file_json2) == result_for_stylish
    assert generate_diff(file_yml1, file_yml2) == result_for_stylish
    assert generate_diff(file_json1, file_json2, format='plain') == result_for_plain
    assert generate_diff(file_yml1, file_yml2, format='plain') == result_for_plain
    assert generate_diff(file_yml1, file_yml2, format='json') == result_for_json


