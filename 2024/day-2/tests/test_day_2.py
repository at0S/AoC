import sys

sys.path.insert(0, "/Users/at0S/github.com/AoC/2024/day-2")

from day_2 import validate_diff, validate_asc, validate_desc, validate_set


def test_diff_simple_1():
    assert validate_diff([1, 2, 3, 4, 5], 3) == True


def test_diff_simple_2():
    assert validate_diff([10, 20, 30, 40, 50], 3) == False


def test_diff_simple_3():
    assert validate_diff([20, 19, 16, 15, 12, 9], 3) == True


def test_validate_asc_1():
    assert validate_asc([1, 2, 3, 4, 5]) == True


def test_validate_asc_2():
    assert validate_asc([5, 4, 3, 2, 1]) == False


def test_validate_asc_3():
    assert validate_asc([20, 19, 16, 15, 12, 9]) == False


def test_validate_desc_1():
    assert validate_desc([5, 4, 3, 2, 1]) == True


def test_validate_desc_2():
    assert validate_desc([1, 2, 3, 4, 5]) == False


def test_validate_desc_3():
    assert validate_desc([20, 19, 16, 15, 12, 9]) == True


def test_validate_set_1():
    assert validate_set([1, 2, 3, 4, 5]) == True


def test_validate_set_2():
    assert validate_set([1, 2, 3, 4, 4]) == False
