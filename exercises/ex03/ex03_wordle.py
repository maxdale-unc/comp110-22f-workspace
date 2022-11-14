"""EX03 - Wordle, for real this time!"""

__author__ = "730482280"


def contains_char(word: str, char: str) -> bool:
    """Checks word for a given character."""
    assert len(char) == 1
    i_contains_char: int = 0
    char_exists: bool = False
    while i_contains_char < len(word) and not char_exists:
        if char == word[i_contains_char]:
            char_exists = True
        else:
            i_contains_char += 1
    if char_exists:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Codifies similarities between two strings in emoji string output."""
    assert len(guess) == len(secret)
    green_box: str = ("\U0001F7E9")
    yellow_box: str = ("\U0001F7E8")
    white_box: str = ("\U00002B1C")
    i_emojified: int = 0
    emojified_output_string: str = ""
    while i_emojified < len(guess):
        if guess[i_emojified] == secret[i_emojified]:
            emojified_output_string += green_box
            i_emojified += 1
        else:
            if contains_char(secret, guess[i_emojified]):
                emojified_output_string += yellow_box
                i_emojified += 1
            else:
                emojified_output_string += white_box
                i_emojified += 1
    return emojified_output_string


def input_guess(expected_length: int) -> str:
    """Prompts user for input and rejects input of incorrect length."""
    user_input: str = input("Enter a " + str(expected_length) + " character word: ")
    while len(user_input) != expected_length:
        user_input = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return user_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn_number: int = 1
    is_solved: bool = False
    guess: str = ""
    while turn_number <= 6 and not is_solved:
        print("=== Turn " + str(turn_number) + "/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            is_solved = True
        else:
            turn_number += 1
    if is_solved:
        print("You won in " + str(turn_number) + "/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()