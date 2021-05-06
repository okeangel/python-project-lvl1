"""Progression game."""

from random import randint

DESCRIPTION = 'What number is missing in the progression?'
MAX_PROG_START_NUMBER = 50
MIN_PROG_LENGTH = 5
MAX_PROG_LENGTH = 15


def generate_progression():
    """Generate the rising arithmetic proression.

    Returns:
        (List) artithmetic progression.
    """
    start = randint(0, MAX_PROG_START_NUMBER)  # noqa: S311
    increment = randint(1, 9)  # noqa: S311
    lenght = randint(MIN_PROG_LENGTH, MAX_PROG_LENGTH)  # noqa: S311

    return [str(start + increment * index) for index in range(lenght)]


def generate_question():
    """Generate the question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    progression = generate_progression()  # noqa: S311

    position = randint(0, len(progression))  # noqa: S311
    correct_answer = progression[position]
    progression[position] = '..'

    question = ' '.join(progression)
    return question, correct_answer
