"""EX06 - Choose your own adventure!"""


from random import randint
import time


__author__ = "730482280"


"""Unicode stuff and formatting."""

RAM: str = "\U0001F411"
SUN: str = "\U00002600"
HEART: str = "\U0001F499"
BRAIN: str = "\U0001F9E0"
MONEY: str = "\U0001F4B0"
ARROW: str = "\U000027A1"
DIVIDER: str = "--------------------------------------------"


"""Days of the week."""

WEEKDAYS: list[str] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


"""Main stats."""


health: int = 3
sanity: int = 3
money: int = 3
points: int = 0


"""Player name."""


player: str = ""


"""Invalid input variables."""


NULL: str = "Invalid choice."
valid_input: bool = False


def main() -> None:
    """Main game."""
    global health
    global sanity
    global money
    global player
    global ARROW
    global NULL
    global valid_input
    points = overall_points_calculator(health, sanity, money)
    greet()
    for day in WEEKDAYS:
        print_delay()
        print(DIVIDER)
        print(f"{SUN} Good morning, {player}! It's {day}! {SUN}")
        print_stats()
        print(DIVIDER)
        course_quantity: int = randint(1, 5)
        classes_number: str = "classes"
        if course_quantity == 1:
            classes_number = "class"
        print_delay()
        print(f"You have {course_quantity} {classes_number} today!")
        while not valid_input:
            print_delay()
            morning: str = ""
            morning = input(f"{ARROW} Do you get up early (1), take your chances and sleep in (2), or drop out of college to join a cult (3)?\n# ")
            if morning == str(3):
                morning_choice_cult()
                valid_input = True
            else:
                if morning == str(2):
                    while not valid_input:
                        print_delay()
                        overslept: str = ""
                        overslept = input(f"{ARROW} Roll the dice to see if you overslept! Pick a number between 1 and 6.\n# ")
                        if int(overslept) > 6 or int(overslept) < 1:
                            print(NULL)
                        else:
                            valid_input = True
                    overslept = int(overslept)
                    morning_choice_sleep_in(overslept_generator(overslept, points))
                else:
                    if morning == str(1):
                        morning_choice_early()
                        valid_input = True
                    else:
                        print(NULL)
        valid_input = False
        i_courses: int = 0
        while i_courses < course_quantity:
            mindless_activity: str = ""
            mindless_activity = mindless_activity_generator(randint(0, 5))
            while not valid_input:
                print_delay()
                print("You take your seat in class.")
                print_delay()
                course_action: str = ""
                course_action = input(f"{ARROW} Do you pay attention (1) or {mindless_activity} instead (2)?\n# ")
                if course_action == str(2):
                    print_delay()
                    print("You are clearly getting a good value for your tuition money.")
                    valid_input = True
                else:
                    if course_action == str(1):
                        course_reaction: int = randint(0, 1)
                        if course_reaction == 0:
                            print_delay()
                            print("Welp, that was a mistake.")
                            print_delay()
                            print("You get overwhelmed and stress yourself out.")
                            sanity -= 1
                        else:
                            print_delay()
                            print("Look at you go!")
                            print_delay()
                            print("You feel confident in your understanding of the content.")
                            sanity += 1
                        valid_input = True
                    else:
                        print(NULL)
            valid_input = False
            is_assignment: int = randint(0, 1)
            if is_assignment == 1:
                print_delay()
                print("Your professor gives you an assignment.")
                sanity -= 1
                print_delay()
                print("You head out.")
            else:
                print_delay()
                print("You head out.")
            is_dog: int = randint(0, 16)
            while is_dog == 0 and not valid_input:
                print_delay()
                print("On your way, you see a dog.")
                pet_dog: str = ""
                pet_dog = input(f"{ARROW} Do you pet it? (Yes/No)\n# ")
                if pet_dog == str("Yes"):
                    print_delay()
                    print("You feel a sense of calmness envelop you. Who's a good boy?")
                    sanity += 1
                    valid_input = True
                else:
                    if pet_dog == str("No"):
                        print_delay()
                        print("You monster.")
                        valid_input = True
                    else:
                        print(NULL)
            valid_input = False
            is_thirsty: int = randint(1, 3)
            if is_thirsty == 2:
                print_delay()
                print("You're a bit thirsty.")
                print_delay()
                print("You grab a drink from the drinking fountain in your downtime.")
                print_delay()
                print("Let's hope there's no lead in it!")
                is_lead: int = randint(1, 5)
                if is_lead == 2:
                    health -= 3
                else:
                    health += 1
            i_courses += 1
        if check_if_dead(health, sanity, money):
            print_delay()
            print(DIVIDER)
            print_stats()
            print(DIVIDER)
            print_delay()
            quit()
        else:
            print_delay()
            print(f"Congrats! You've made it through {day}.")
            print_delay()
            print("You head home.")
    print_delay()
    print(f"{DIVIDER}\nCongrats! You've made it through the week!\n{DIVIDER}")
    quit()


def greet() -> None:
    """Greets the user and describes the game."""
    global ARROW
    global DIVIDER
    global NULL
    global player
    print(f"{DIVIDER}\n{RAM} Welcome to UNC Chapel Hill Simulator! {RAM}\nSurvive a week as a college student!\n{DIVIDER}")
    print_delay()
    player = input(f"{ARROW} Welcome! What is your name?\n# ")


def overall_points_calculator(health: int, sanity: int, money: int) -> int:
    """Calculates overall points as an integer average based on the three individual game metrics."""
    points: int = 0
    points = ((health + sanity + money) // 3)
    return points


def print_stats() -> None:
    """Prints currently calculated player stats."""
    global health
    global sanity
    global money
    print(f"{HEART} Health: {health}\n{BRAIN} Sanity: {sanity}\n{MONEY} Money: {money}\nOverall points: " + str(overall_points_calculator(health, money, sanity)))


def check_if_dead(input_health: int, input_sanity: int, input_money: int) -> bool:
    """Checks if player has died based on if any of their stats have hit zero."""
    if input_health <= 0:
        print("You died! Game over.")
        return True
    else:
        if input_sanity <= 0:
            print("You went insane! Game over.")
            return True
        else:
            if input_money <= 0:
                print("You went broke! Game over")
                return True
            else:
                return False


def print_delay() -> None:
    """Adds a half-second delay - for use between print statements."""
    time.sleep(0.75)


"""Proceedures for choices player can make every morning."""


def morning_choice_early() -> None:
    """Confirms early morning selection and adjusts score."""
    global health
    global sanity
    print_delay()
    print("Look at you go!")
    print_delay()
    print("You make yourself a nice coffee and get settled into your day, but you're still a little tired. At least the sunrise was pretty.")
    health -= 1
    sanity += 1
    print_delay()
    valid_input = False
    while not valid_input:
        class_early: str = ""
        class_early = input("Do you go to class early? (Yes/No)\n# ")
        if class_early == str("Yes"):
            print_delay()
            print("You make it to class early.")
            valid_input = True
        else:
            if class_early == str("No"):
                print_delay()
                print("Yeah, relax a little bit!")
                print_delay()
                print("It's not like you're a nerd or something.")
                sanity += 1
                valid_input = True
            else:
                print(NULL)


def morning_choice_sleep_in(roll: int) -> None:
    """Confirms sleep in selection and adjusts score."""
    global health
    global sanity
    global money
    global player
    if roll == 1:
        print_delay()
        print("You woke up in time for class!")
        print_delay()
        print(f"Good job, {player}.")
        print_delay()
        print("The extra sleep nourishes you, and you make it to class on time.")
        health += 1
    else:
        if roll == 2:
            print_delay()
            print(f"Yikes, {player}! You overslept.")
            print_delay()
            print("You were almost late for class, but made it on time by renting a scooter.")
            print_delay()
            print("The sleep heals you, but the scooter costs money.")
            health += 1
            money -= 1
        else:
            print_delay()
            print(f"Yikes, {player}! You overslept.")
            print_delay()
            print("In spite of renting a scooter, you still didn't make it on time.")
            print_delay()
            print("The sleep heals you, but the scooter costs money and your professor seems irritated with you.")
            health += 1
            sanity -= 1
            money -= 1


def overslept_generator(user_roll: int, user_points: int) -> int:
    """Decides if user oversleeps or not based on guess."""
    global points
    computer_roll: int = randint(1, 6)
    if computer_roll == user_roll or (user_points - computer_roll) == user_roll:
        return int(1)
    else:
        if computer_roll > user_roll:
            return int(2)
        else:
            if computer_roll < user_roll:
                return int(3)


def morning_choice_cult() -> None:
    """Confirms cult selection, displays final score, and quits."""
    print_delay()
    print(DIVIDER)
    print("Hope you like Kool-Aid! Good luck with that.")
    print_stats()
    print(DIVIDER)
    print("Game over.")
    quit()


def mindless_activity_generator(index: int) -> str:
    """Stores a list of mindless activities and spits one out given an index."""
    options: list[str] = ["scroll Twitter on your laptop", "daydream about faking your death and becoming a hermit in the woods", "doodle a sick space ship in your notebook", "read the entire Wikipedia page for rope", "cause mayhem on Chatroulette", "play CoolMathGames"]
    return options[index]


if __name__ == "__main__":
    main()
