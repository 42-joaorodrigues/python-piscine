import sys


def parse_args(args: list) -> tuple:
    """Return (S, N) from the command line, or raise AssertionError."""
    assert len(args) == 3, "the arguments are bad"
    try:
        n = int(args[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    return args[1], n


def main():
    """Print the words of S longer than N."""
    try:
        s, n = parse_args(sys.argv)
        print([word for word in filter(lambda w: len(w) > n, s.split())])
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
