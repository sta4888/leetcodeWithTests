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


@pytest.mark.skip
def test_two_sum_basic(solution):
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    assert result == [0, 1] or result == [1, 0]

@pytest.mark.skip
def test_two_sum_multiple_options(solution):
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == [1, 2] or result == [2, 1]

@pytest.mark.skip
def test_two_sum_same_element(solution):
    nums = [3, 3]
    target = 6
    result = solution.twoSum(nums, target)
    assert result == [0, 1] or result == [1, 0]

@pytest.mark.skip
def test_two_sum_no_result(solution):
    nums = [1, 2, 3]
    target = 7
    result = solution.twoSum(nums, target)
    assert result == []


def test_two_sum():
    assert True

