"""Exercise 02: add one argparse option to a small CLI."""

import argparse


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    result.add_argument("--turn", required=True, type=int, help="Turn number (integer)")
    return result


def main() -> None:
    """Parse learner arguments and display the resulting namespace."""
    print(parser().parse_args())


if __name__ == "__main__":
    main()
