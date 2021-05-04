"""Parity Check game."""

import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MAX_NUMBER_IN_CALCULATION = 99


def generate_question():
    """Generate a question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    question = random.randrange(MAX_NUMBER_IN_CALCULATION)  # noqa: S311
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
