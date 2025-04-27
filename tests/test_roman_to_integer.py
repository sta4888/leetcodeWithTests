import pytest

from Easy.roman_to_integer import Solution


@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("num, expect", [
    ("III", 3),
    ("IV", 4),
    ("VI", 6),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
])
def test_roman_to_int(solution, num, expect):
    result = solution.romanToInt(num)
    assert result == expect
