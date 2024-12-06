import sys
sys.path.insert(0, "/Users/at0S/github.com/AoC/2024/day-5")

from  day_5 import get_list_midsection, process_print_order

def test_get_list_midsection_1():
    assert get_list_midsection(["1", "2", "3", "4", "5"]) == 3

def test_get_list_midsection_2():
    assert get_list_midsection(["1", "2", "3", "4", "5", "6","7","8","9","10","11"]) == 6

def test_get_list_midsection_3():
    assert get_list_midsection(['97', '75', '47', '29', '13']) == 47

def test_process_print_order():
    order={'47': ['53', '13', '61', '29'], '97': ['13', '61', '47', '29', '53', '75'], '75': ['29', '53', '47', '61', '13'], '61': ['13', '53', '29'], '29': ['13'], '53': ['29', '13']}
    sequence = ['97','13','75','29','47']
    assert process_print_order(sequence, order) == ['97', '75', '47', '29', '13']
