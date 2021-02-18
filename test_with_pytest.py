import pytest
from main import Action

CHOICES = [action.value for action in Action]
ANSWER = {
        Action.Paper: [Action.Rock],
        Action.Rock: [Action.Scissors],
        Action.Scissors: [Action.Paper]
    }


@pytest.fixture()
def user_computer_selection():
    import random
    user = random.randint(0, len(CHOICES)-1)
    computer = random.randint(0, len(CHOICES) - 1)
    return Action(user), Action(computer)


def test_user_input_validity(user_computer_selection):
    user, computer = user_computer_selection
    assert user.value in CHOICES


def test_user_input_not_in_action():
    user_input = 4
    assert user_input not in CHOICES


def test_user_win_situation():
    user = Action.Paper
    computer = Action.Rock
    assert computer in ANSWER[user]


def test_computer_win_situation():
    computer = Action.Paper
    user = Action.Rock
    assert user in ANSWER[computer]


def test_draw_situation(user_computer_selection):
    assert user_computer_selection[0] == user_computer_selection[1]





