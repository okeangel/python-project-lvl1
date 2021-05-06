#!/usr/bin/env python
"""Run the Brain-Calc game."""

from brain_games import engine
from brain_games.games import gcd


def main():
    """Run the game."""
    engine.play(gcd)


if __name__ == '__main__':
    main()
