#!/usr/bin/env python
"""Run the Brain-Calc game."""

from brain_games import engine
from brain_games.games import prime


def main():
    """Run the game."""
    engine.play(prime)


if __name__ == '__main__':
    main()
