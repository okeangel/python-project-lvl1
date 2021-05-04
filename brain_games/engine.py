"""Provide main game flow."""

import prompt


def welcome_user() -> str:
    """Get user name from input.

    Returns:
        user name.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name


def play(game, rounds: int = 3):
    """Play several identical rounds of the game.

    Args:
        game: a complete module with special attributes.

        rounds: Maximum number of rounds. Game will end  # noqa: DAR101
            when player fails a round, or when player reach
            the maximum of rounds.

    Returns:
        None.
    """
    player_name = welcome_user()
    print(game.DESCRIPTION)

    while rounds:
        question, correct_answer = game.generate_question()
        print('Question: {0}'.format(question))

        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print("'{0}' is wrong answer ;(. ".format(answer), end='')
            print("Correct answer was '{0}'.".format(correct_answer))
            print("Let's try again, {0}!".format(player_name))
            return None

        print('Correct!')
        rounds -= 1

    print('Congratulations, {0}!'.format(player_name))
    return None
