#!/usr/bin/env python
"""Calculator game."""

import random

from brain_games import game_flow

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER_IN_CALCULATION = 99
OPERATIONS = ('+', '-', '*')


def generate_a_question():
    """Generate the question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    first = random.randrange(MAX_NUMBER_IN_CALCULATION)  # noqa: S311
    second = random.randrange(MAX_NUMBER_IN_CALCULATION)  # noqa: S311
    operation = random.choice(OPERATIONS)  # noqa: S311
    question = ' '.join([str(first), operation, str(second)])
    return question, str(eval(question))  # noqa: S307


def main():
    """Process the game."""
    game_flow.play(generate_a_question, DESCRIPTION)


if __name__ == '__main__':
    main()
