"""Parity Check game."""

import random

import prompt
from brain_games import cli

MAX_QUESTION = 99


def play():
    """Game play function.

    Returns:
        None
    """
    user_name = cli.welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        question = random.randrange(MAX_QUESTION)  # noqa: S311
        print('Question: {0}'.format(question))

        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        answer = prompt.string(prompt='Your answer: ')

        if answer != correct_answer:
            print("'{0}' is wrong answer ;(. ".format(answer), end='')
            print("Correct answer was '{0}'.".format(correct_answer))
            print("Let's try again, {0}!".format(user_name))
            return None

        print('Correct!')
        count += 1

    print('Congratulations, {0}!'.format(user_name))
    return None


if __name__ == '__main__':
    play()
