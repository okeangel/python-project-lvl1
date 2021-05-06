#!/usr/bin/env python
"""Run the Brain-Calc game."""

from brain_games import engine
from brain_games.games import progression


def main():
    """Run the game."""
    engine.play(progression)


if __name__ == '__main__':
    main()
