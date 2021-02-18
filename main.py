# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


def get_user_selection():
    choices = ', '.join([f"{action.name}[{action.value}]" for action in Action])
    user_input = int(input(f"Enter a choice ({choices}): "))
    action = Action(user_input)
    return action


def get_computer_selection():
    import random
    random_int = random.randint(0, len(Action)-1)
    action = Action(random_int)
    return action


def determine_winner(user, computer):
    answer = {
        Action.Paper: [Action.Rock],
        Action.Rock: [Action.Scissors],
        Action.Scissors: [Action.Paper]
    }

    defeat = answer[user]

    if user == computer:
        print(f"YOU: {user.name} Vs COMPUTER: {computer.name} = It's a tie")
    elif computer in defeat:
        print(f"YOU: [{user.name}] Vs COMPUTER: {computer.name} = You win!")
    else:
        print(f"YOU: {user.name} Vs COMPUTER: [{computer.name}] = You lose")


def play_game():

    while True:
        user_selection = get_user_selection()

        computer_selection = get_computer_selection()

        determine_winner(user_selection, computer_selection)

        user_input = input("Play again? Y/N : ")
        if user_input.upper() == 'N':
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()

