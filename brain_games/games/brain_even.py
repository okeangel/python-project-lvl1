#!/usr/bin/env python
"""Parity Check game."""

import random

from brain_games import game_flow

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER_IN_CALCULATION = 99


def generate_a_question():
    """Generate the question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    question = random.randrange(MAX_NUMBER_IN_CALCULATION)  # noqa: S311
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def main():
    """Process the game."""
    game_flow.play(generate_a_question, DESCRIPTION)


if __name__ == '__main__':
    main()
