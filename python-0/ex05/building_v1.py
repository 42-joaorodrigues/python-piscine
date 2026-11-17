import sys
import string


def prompt_user():
    """Prompt user for input"""
    print("What is the text to count?")
    return sys.stdin.read()


def input_parser(args: list[str]) -> str:
    """Return argument or ask for input.
    Raises AssertionError"""
    if len(args) < 2:
        return prompt_user()
    assert len(args) == 2, "more than one argument provided"
    if len(args[1]) == 0:
        return prompt_user()
    return args[1]


def count_characters(s: str):
    """Return dict with character counts"""
    counts = {
        "total": 0,
        "uppers": 0,
        "lowers": 0,
        "punctuations": 0,
        "spaces": 0,
        "digits": 0,
    }
    for c in s:
        counts["total"] += 1
        if c.isupper():
            counts["uppers"] += 1
        elif c.islower():
            counts["lowers"] += 1
        elif c in string.punctuation:
            counts["punctuations"] += 1
        elif c.isspace():
            counts["spaces"] += 1
        elif c.isdigit():
            counts["digits"] += 1
    return counts


def main():
    """Count characters in a given string"""
    try:
        user_input = input_parser(sys.argv)
        counts = count_characters(user_input)

        print(f"The text contains {counts['total']} characters:")
        print(f"{counts['uppers']} upper letters")
        print(f"{counts['lowers']} lower letters")
        print(f"{counts['punctuations']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
