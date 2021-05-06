"""Progression game."""

from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MAX_NUMBER = 99


def is_prime(number):  # noqa: WPS 231
    """Generate the rising prime sequence.

    Create a positive number range at first, and test each number
    is it a prime.

    Args:
        number: the maximal number should be tested.

    Returns:
        (List) prime sequence.
    """
    primes = []
    numbers = list(range(2, (number // 2) + 1))
    while numbers:
        current = numbers.pop(0)
        current_is_prime = True

        for prime in primes:
            if current % prime == 0:
                current_is_prime = False
                break

        if current_is_prime:
            if number % current == 0:
                return False

            primes.append(current)

    return True


def generate_question():
    """Generate the question.

    Returns:
        Tuple(question: str, correct_answer: str).
    """
    number = randint(2, MAX_NUMBER)  # noqa: S311
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'

    return question, correct_answer
