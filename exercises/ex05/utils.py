"""EX05 - List utilities and unit testing!"""


__author__ = "730482280"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns only even integer values in a given list."""
    output_list: list[int] = list()
    i: int = 0
    while i <= (len(input_list) - 1):
        if input_list[i] % 2 == 0:
            output_list.append(input_list[i])
        i += 1
    return output_list


def concat(input_list_a: list[int], input_list_b: list[int]) -> list[int]:
    """Concatonates two integer lists together."""
    output_list: list[int] = list()
    i_a: int = 0
    while i_a <= (len(input_list_a) - 1):
        output_list.append(input_list_a[i_a])
        i_a += 1
    i_b: int = 0
    while i_b <= (len(input_list_b) - 1):
        output_list.append(input_list_b[i_b])
        i_b += 1
    return output_list


def sub(input_list: list[int], starting_index: int, ending_index: int) -> list[int]:
    """Given a list and a range of indicies, will output list truncated to specified range."""
    output_list: list[int] = list()
    i: int = 1
    if len(input_list) == 0 or starting_index > (len(input_list) - 1) or ending_index <= 0:
        output_list = list()
        return output_list
    if starting_index <= 0:
        i = 0
    else:
        while i != starting_index:
            i += 1
    if ending_index > (len(input_list) - 1):
        ending_index = (len(input_list))
    lower_boundary: int = int(starting_index)
    upper_boundary: int = int(ending_index - 1)
    while i >= lower_boundary and i <= upper_boundary:
        output_list.append(input_list[i])
        i += 1
    return output_list