#!/usr/bin/env python
"""Run the Brain-Even game."""

from brain_games import engine
from brain_games.games import even


def main():
    """Run the game."""
    engine.play(even)


if __name__ == '__main__':
    main()
