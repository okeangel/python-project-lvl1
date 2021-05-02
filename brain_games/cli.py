"""Provide a Command Line Interface for Brain Games."""

import prompt


def welcome_user():
    """Greet the user.

    Returns:
        user name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
