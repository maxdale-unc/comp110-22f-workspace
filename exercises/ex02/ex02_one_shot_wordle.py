"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730482280"

target_word: str = ("python")
target_word_length: int = len(target_word)
input_word: str = input("What is your " + str(target_word_length) + "-letter guess? ")
i: int = 0

# Unicode output comparing input word to target word
word_comparison: str = ("")

# Unicode characters to append to word comparison
white_box: str = ("\U00002B1C")
green_box: str = ("\U0001F7E9")
yellow_box: str = ("\U0001F7E8")

while len(input_word) != target_word_length:
    print("That was not " + str(target_word_length) + " letters! Try again: ")
    input_word = input("What is your " + str(target_word_length) + "-letter guess? ")

while i < target_word_length:
    if input_word[i] == target_word[i]:
        word_comparison += green_box
    else:
        character_exists: bool = False
        i_character_exists: int = 0
        while not character_exists and i_character_exists < target_word_length:
            if target_word[i_character_exists] == input_word[i]:
                character_exists = True
            else:
                i_character_exists += 1
        if character_exists:
            word_comparison += yellow_box
        else:
            word_comparison += white_box
    i += 1
        
print(word_comparison)

if input_word == target_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")