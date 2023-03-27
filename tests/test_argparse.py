from gendiff.argparse import arg_parse
from unittest.mock import patch


def test_arg_parse_stylish():
    path1 = "tests/fixtures/file1_for_test.json"
    path2 = "tests/fixtures/file2_for_test.json"
    with patch("sys.argv", ["arg_parse", path1, path2]):
        args = arg_parse()
    assert args.format == 'stylish'
    assert args.first_file == 'tests/fixtures/file1_for_test.json'
    assert args.second_file == 'tests/fixtures/file2_for_test.json'


def test_arg_parse_plain():
    path1 = "tests/fixtures/file1_for_test.json"
    path2 = "tests/fixtures/file2_for_test.json"
    with patch("sys.argv", ["arg_parse", "--format", "plain", path1, path2]):
        args = arg_parse()
    assert args.format == 'plain'
    assert args.first_file == 'tests/fixtures/file1_for_test.json'
    assert args.second_file == 'tests/fixtures/file2_for_test.json'


def test_arg_parse_json():
    path1 = "tests/fixtures/file1_for_test.json"
    path2 = "tests/fixtures/file2_for_test.json"
    with patch("sys.argv", ["arg_parse", "--format", "json", path1, path2]):
        args = arg_parse()
    assert args.format == 'json'
    assert args.first_file == 'tests/fixtures/file1_for_test.json'
    assert args.second_file == 'tests/fixtures/file2_for_test.json'
