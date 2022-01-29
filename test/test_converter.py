import pytest

from main import converter, validate_input

str_list = [
    (['4\n', '-2\n', '1\n', '3', '0', '1', '0', '1'],
        [4, -2, 1, 3, 0, 1, 0, 1]),
    (['4', '-2', '1', '3', '0', '1', '0', '1'], [4, -2, 1, 3, 0, 1, 0, 1]),
    (['4', '-2\n', '1\n', '3', 0, 1, 0, 1], [4, -2, 1, 3, 0, 1, 0, 1]),
    ([1, 3], [1, 3]),
    ([], [])
]


@pytest.mark.parametrize('str_list,expected', str_list)
def test_converter(str_list, expected):
    result_list = converter(str_list)
    assert result_list == expected


str_list_no_number = [
    (['3', 'a']),
    (['3\n', 'a\n']),
    (['31-2', '32']),
    (['', '', '', '', '', '', '', ''], []),
    (['2\n', '3\n', 2, 'a', 'p\n'])
]


@pytest.mark.parametrize('str_list', str_list_no_number)
def test_converter_errror_string(str_list):
    with pytest.raises(ValueError):
        converter(str_list)


valid_input = [
    (10, 1, 10, True)
]


@pytest.mark.parametrize('var,min,max,expected', valid_input)
def test_valid_converter(var, min, max, expected):
    assert validate_input(var, min, max) == expected


invalid_input = [
    (10, 1, 6)
]


@pytest.mark.parametrize('var,min,max', invalid_input)
def test_invalid_converter(var, min, max):
    with pytest.raises(ValueError):
        validate_input(var, min, max)
