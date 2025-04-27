from pickle import FALSE

import pytest

from Easy.palindrome_number import Solution


@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("num, expect", [
    (121, True),
    (-121, False),
    (10, False),
])
def test_palindrome(solution, num, expect):
    result = solution.isPalindrome(num)
    assert result == expect

def test_is_palindrome():
    assert True
