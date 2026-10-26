"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Demonstrate choosing an action from the bot core."""
    position = 1
    goal = 4
    action = choose_action(position, goal)
    print(f"Position: {position}, goal: {goal}")
    print(f"Chosen action: {action}")


if __name__ == "__main__":
    main()
