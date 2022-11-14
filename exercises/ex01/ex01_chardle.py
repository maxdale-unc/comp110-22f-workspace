"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730482280"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + letter + " in " + word)

instances: int = 0

if word[0] == letter:
    instances += 1
    print(letter + " found at index 0")

if word[1] == letter:
    instances += 1
    print(letter + " found at index 1")

if word[2] == letter:
    instances += 1
    print(letter + " found at index 2")

if word[3] == letter:
    instances += 1
    print(letter + " found at index 3")

if word[4] == letter:
    instances += 1
    print(letter + " found at index 4")

if instances == 0:
    print("No instances of " + letter + " found in " + word)
else:
    if instances == 1:
        print(str(instances) + " instance of " + letter + " found in " + word)
    else:
        print(str(instances) + " instances of " + letter + " found in " + word)