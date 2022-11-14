"""EX07 - Dictionary functions testing."""


__author__ = "730482280"


from dictionary import invert, favorite_color, count


def test_invert_empty_dict() -> None:
    """Edge case: Empty dictionary is inputted."""
    input: dict[str, str] = dict()
    output: dict[str, str] = dict()
    assert invert(input) == output


def test_invert_arbitrary() -> None:
    """Use case: Arbitrary dictionary is inputted."""
    input: dict[str, str] = {"a": "A", "b": "B", "c": "C"}
    output: dict[str, str] = {"A": "a", "B": "b", "C": "c"}
    assert invert(input) == output


def test_invert_uncode() -> None:
    """Use case: Unicode dictionary is inputted."""
    input: dict[str, str] = {"\U00002B1C": "\U0001F7E9"}
    output: dict[str, str] = {"\U0001F7E9": "\U00002B1C"}
    assert invert(input) == output


def test_favorite_color_different() -> None:
    """Edge case: Everybody has different favorite colors."""
    input: dict[str, str] = {"Max": "red", "Jake": "green", "Lexi": "yellow", "Shayla": "blue"}
    output: str = "red"
    assert favorite_color(input) == output


def test_favorite_color_tie() -> None:
    """Use case: There is a tie for favorite color."""
    input: dict[str, str] = {"Max": "red", "Shelby": "red", "Jake": "green", "Dan": "green"}
    output: str = "red"
    assert favorite_color(input) == output


def test_favorite_color_arbitrary() -> None:
    """Use case: An arbitrary list is inputted."""
    input: dict[str, str] = {"Max": "red", "Jake": "green", "Dan": "green", "Lexi": "yellow"}
    output: str = "green"
    assert favorite_color(input) == output


def test_count_empty() -> None:
    """Edge case: Empty list is inputted."""
    input: list[str] = list()
    output: dict[str, int] = dict()
    assert count(input) == output


def test_count_repeats() -> None:
    """Use case: A list is inputted that contains repeated items."""
    input: list[str] = ["Max", "Jake", "Shelby", "Jake", "Shelby"]
    output: dict[str, int] = {"Max": 1, "Jake": 2, "Shelby": 2}
    assert count(input) == output


def test_count_no_repeats() -> None:
    """Use case: A list is inputted in which all items all appear once."""
    input: list[str] = ["Max", "Jake", "Shelby", "Corey", "Hannah"]
    output: dict[str, int] = {"Max": 1, "Jake": 1, "Shelby": 1, "Corey": 1, "Hannah": 1}
    assert count(input) == output