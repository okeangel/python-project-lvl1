"""Greatest Common Divider game."""

from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MAX_NUMBER = 100


def gcd(a, b):  # noqa: WPS111
    """Call a function to calculate greatest common divider.

    Args:
        a: first number
        b: second number

    Returns:
        the greatest common divider.
    """
    if b > a:
        a, b = b, a  # noqa: WPS111
    return euclid_gcd(a, b)


def euclid_gcd(a, b):  # noqa: WPS111
    """Calculate the greatest common divider using Euclidian algoritm.

    Args:
        a: first number
        b: second number

    Returns:
        the greatest common divider.
    """
    while True:
        remainder = a % b
        if remainder == 0:
            return b
        a, b = b, remainder  # noqa: WPS111


def my_gcd(a, b):  # noqa: WPS111
    """Calculate the greatest common divider.

    Args:
        a: first number,
        b: second number.

    Returns:
        the greatest common divider.
    """
    current = a // 2
    if current > b:
        current = b

    while current > 1:
        if a % current == 0 and b % current == 0:
            return current
        current -= 1

    return current


def generate_question():
    """Generate the question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    first = randint(1, MAX_NUMBER)  # noqa: S311
    second = randint(1, MAX_NUMBER)  # noqa: S311
    question = ' '.join([str(first), str(second)])
    correct_answer = gcd(first, second)
    return question, str(correct_answer)
