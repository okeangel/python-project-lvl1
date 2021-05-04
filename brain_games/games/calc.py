"""Calculator game."""

from random import choice, randrange

DESCRIPTION = 'What is the result of the expression?'
MAX_NUMBER = 99
OPERATIONS = ('+', '-', '*')


def generate_question():
    """Generate the question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    first = randrange(MAX_NUMBER)  # noqa: S311
    second = randrange(MAX_NUMBER)  # noqa: S311
    operation = choice(OPERATIONS)  # noqa: S311
    question = ' '.join([str(first), operation, str(second)])
    return question, str(eval(question))  # noqa: S307
