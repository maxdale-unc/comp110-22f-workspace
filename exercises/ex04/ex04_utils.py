"""EX04 - Making Picasso proud (except that he's dead, and like - can't be. You know what I mean)!"""


__author__ = "730482280"


def all(input_list_all: list[int], input_int: int) -> bool:
    """Determines if all values in an inputted list are equal to a given integer."""
    if len(input_list_all) == 0:
        return False
    i_all: int = 0
    all_equal: bool = True
    while i_all <= (len(input_list_all) - 1) and all_equal:
        if input_int != input_list_all[i_all]:
            all_equal = False
        else:
            i_all += 1
    if all_equal:
        return True
    else:
        return False


def max(input_list_max: list[int]) -> int:
    """Determines the largest value in a list."""
    if len(input_list_max) == 0:
        raise ValueError("max() arg is an empty List")
    i_max: int = 0
    max_value: int = input_list_max[i_max]
    while i_max <= (len(input_list_max) - 1):
        if max_value <= input_list_max[i_max]:
            max_value = input_list_max[i_max]
            i_max += 1
        else:
            i_max += 1
    return max_value


def is_equal(input_list_is_equal_a: list[int], input_list_is_equal_b: list[int]) -> bool:
    """Determines if two lists are deeply equal."""
    if input_list_is_equal_a == input_list_is_equal_b:
        return True
    else:
        return False