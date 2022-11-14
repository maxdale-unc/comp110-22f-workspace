"""EX05 - List utilities and unit testing!"""


__author__ = "730482280"


from utils import only_evens, sub, concat


def test_only_evens_arbitrary_input() -> None:
    """Use case: List of arbitrary list values are inputted."""
    input: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    assert only_evens(input) == [2, 4, 6, 8, 0]


def test_only_evens_odd_only_input() -> None:
    """Use case: List of only odd numbers is inputted."""
    input: list[int] = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert only_evens(input) == list()


def test_only_evens_empty_input() -> None:
    """Edge case: Empty list is inputted."""
    input: list[int] = list()
    assert only_evens(input) == list()


def test_concat_arbitrary_input() -> None:
    """Use case: Two lists with arbitrary values are inputted."""
    input_a: list[int] = [1, 2, 3, 4, 5]
    input_b: list[int] = [6, 7, 8, 9, 0]
    assert concat(input_a, input_b) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def test_concat_one_empty_input() -> None:
    """Use case: One empty list and one populated list are inputted."""
    input_a: list[int] = [1, 2, 3, 4, 5]
    input_b: list[int] = list()
    assert concat(input_a, input_b) == [1, 2, 3, 4, 5]


def test_concat_two_empty_input() -> None:
    """Edge case: Two empty lists are inputted."""
    input_a: list[int] = list()
    input_b: list[int] = list()
    assert concat(input_a, input_b) == list()


def test_sub_boundaries_in_range() -> None:
    """Use case: Inputted boundaries are both within range of list indicies."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lower_boundary: int = 2
    upper_boundary: int = 7
    assert sub(input_list, lower_boundary, upper_boundary) == [2, 3, 4, 5, 6]


def test_sub_empty_list() -> None:
    """Use case: Empty list is inputted with (inherently) out-of-range boundaries."""
    input_list: list[int] = list()
    lower_boundary: int = 3
    upper_boundary: int = 8
    assert sub(input_list, lower_boundary, upper_boundary) == list()


def test_sub_negative_lower_bound() -> None:
    """Edge case: Lower boundary is negative."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lower_boundary: int = -14
    upper_boundary: int = 5
    assert sub(input_list, lower_boundary, upper_boundary) == [1, 2, 3, 4]


def test_sub_large_upper_bound() -> None:
    """Edge case: Lower boundary is negative."""
    input_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lower_boundary: int = 5
    upper_boundary: int = 17
    assert sub(input_list, lower_boundary, upper_boundary) == [5, 6, 7, 8, 9]