import sys
sys.path.insert(0, "/Users/at0S/github.com/AoC/2024/day-5")

from  day_5 import get_list_midsection

def test_get_list_midsection_1():
    assert get_list_midsection(["1", "2", "3", "4", "5"]) == 3

def test_get_list_midsection_2():
    assert get_list_midsection(["1", "2", "3", "4", "5", "6","7","8","9","10","11"]) == 6
