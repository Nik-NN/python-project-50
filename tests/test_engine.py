import pytest
from gendiff.generate_diff import generate_diff


file_json1 = 'tests/fixtures/file1_for_test.json'
file_json2 = 'tests/fixtures/file2_for_test.json'
file_yml1 = 'tests/fixtures/file1_for_test.yml'
file_yml2 = 'tests/fixtures/file2_for_test.yml'
file_txt1 = 'tests/fixtures/file1_for_test.txt'
file_txt2 = 'tests/fixtures/file2_for_test.txt'
result_for_stylish = open("tests/fixtures/result_for_stylish.txt", "r").read()
result_for_plain = open("tests/fixtures/result_for_plain.txt", "r").read()
with open("tests/fixtures/result_for_json.json", "r") as my_file:
    result_for_json = my_file.read()


@pytest.mark.parametrize("test_input_1,test_input_2,format,expected", [
    (file_json1, file_json2, 'stylish', result_for_stylish),
    (file_yml1, file_yml2, 'stylish', result_for_stylish),
    (file_json1, file_yml2, 'stylish', result_for_stylish),
    (file_json1, file_json2, 'plain', result_for_plain),
    (file_yml1, file_yml2, 'plain', result_for_plain),
    (file_json1, file_json2, 'json', result_for_json),
    (file_yml1, file_yml2, 'json', result_for_json),
    (file_txt1, file_txt2, 'stylish', result_for_stylish)])
def test_generate_diff(test_input_1, test_input_2, format, expected):
    assert generate_diff(test_input_1, test_input_2, format) == expected
