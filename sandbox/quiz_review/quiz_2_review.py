def odd_and_even(input: list[int]) -> list[int]:
    output_list: list[int] = []
    i: int = 0
    while i < len(input):
        if (input[i] % 2) != 0 and (i % 2) == 0:
            output_list.append(input[i])
        i += 1
    return output_list

"""print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))"""

def vowels_and_threes(input: str) -> str:
    """doctstring"""
    output: str = ""
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    i = 0
    while i < len(input):
        if input[i] in vowels and (i % 3) == 0:
            i += 1
        else:
            if input[i] in vowels or (i % 3) == 0:
                output += input[i]
                i += 1
            else:
                i += 1
    return output

"""print(vowels_and_threes("hello world"))"""

def best_animals(input: dict[str, list[int]]) -> list[int]:
    """"""
    for animal in input:
        