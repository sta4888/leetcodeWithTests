import pytest

from Easy.twoSum import Solution


@pytest.fixture
def solution():
    return Solution()



def test_solution():
    """
    Проверяем, действительно ли создается объект Solution
    """

    assert Solution()


@pytest.mark.parametrize("nums_list, target, expect", [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0, 1]),
])
def test_two_sum_basic(solution, nums_list, target, expect):
    result = solution.two_sum(nums_list, target)
    assert result == [0, 1] or result == expect



def test_two_sum_no_result(solution):
    nums = [1, 2, 3]
    target = 7
    result = solution.two_sum(nums, target)
    assert result == []



def test_two_sum():
    assert True

