import pytest
from gendiff.generate_diff import generate_diff


file_json1 = 'tests/fixtures/file1_for_test.json'
file_json2 = 'tests/fixtures/file2_for_test.json'
file_yml1 = 'tests/fixtures/file1_for_test.yml'
file_yml2 = 'tests/fixtures/file2_for_test.yml'
file_wrong_format = 'tests/fixtures/file1_for_test.txt'
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
    (file_yml1, file_yml2, 'json', result_for_json)])
def test_generate_diff(test_input_1, test_input_2, format, expected):
    assert generate_diff(test_input_1, test_input_2, format) == expected


def test_exception_open_files():
    with pytest.raises(Exception) as e:
        generate_diff(file_wrong_format, file_json2)
    exception_text = 'Wrong format.\nInput formats: yaml, json.'
    assert str(e.value) == exception_text


def test_exception_generate_diff():
    with pytest.raises(Exception) as e:
        generate_diff(file_json1, file_json2, 'plainf')
    exception_text = 'Wrong format.\nReport as plain text, stylish and json'
    assert str(e.value) == exception_text
