import sys

sys.path.insert(0, "/Users/at0S/github.com/AoC/2024/day-3")

from day_3 import complex_processing, simple_multiply, more_complex_processing


def test_complex_processing():
    assert (
        complex_processing(
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
            "don't()",
        )
        == "xmul(2,4)&mul[3,7]!^?mul(8,5))"
    )


def test_more_complex_processing():
    assert (
        more_complex_processing(
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        )
        == "xmul(2,4)&mul[3,7]!^?mul(8,5))"
    )


def test_simple_multiply():
    assert simple_multiply("xmul(2,4)&mul[3,7]!^?mul(8,5))") == 48


def test_more_complex_processing_1():
    assert (
        more_complex_processing("aaaaadon't()bbbbbdon't()do()cccccdo()") == "aaaaaccccc"
    )
