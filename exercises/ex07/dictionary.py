"""EX07 - Dictionary functions."""

__author__ = "730482280"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and associated values of a dictionary."""
    output_dict = dict()
    for key in input_dict:
        value: str = input_dict[key]
        if value in output_dict:
            raise KeyError("Invalid: Duplicate key in output.")
        output_dict[value] = key
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Determines the most common value in a dictionary, and returns the first one if there is a tie."""
    tally_dict: dict[str, int] = dict()
    for name in input_dict:
        color: str = ""
        color = input_dict[name]
        instances: int = 0
        for name in input_dict:
            if str(color) == str(input_dict[name]):
                instances += 1
        duplicates: int = 0
        i_duplicates = 0
        while i_duplicates < len(tally_dict):
            for entry in tally_dict:
                if color == entry:
                    duplicates += 1
            i_duplicates += 1
        if duplicates == 0:
            tally_dict[str(color)] = instances
    reverse_tally_dict: dict[int, str] = dict()
    for color in tally_dict:
        frequency: int = tally_dict[color]
        if tally_dict[color] not in reverse_tally_dict:
            reverse_tally_dict[frequency] = color
    greatest_frequency: int = max(reverse_tally_dict)
    favorite_color: str = ""
    for color in tally_dict:
        if tally_dict[color] == greatest_frequency:
            favorite_color = color
            break
    return favorite_color


def count(input_list: list[str]) -> dict[str, int]:
    """Takes an input list and creates a dictionary in which the list values are the values and the position in the list is the key."""
    output_dict: dict[str, int] = dict()
    for value in input_list:
        if value in output_dict:
            output_dict[value] += 1
        else:
            output_dict[value] = 1
    return output_dict