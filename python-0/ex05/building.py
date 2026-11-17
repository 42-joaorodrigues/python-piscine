import sys
import string


def main():
    """Count characters in a given string"""
    try:
        assert len(sys.argv) <= 2, "more than one argument provided"
        if len(sys.argv) < 2 or len(sys.argv[1]) == 0:
            print("What is the text to count?")
            s = sys.stdin.read()
        else:
            s = sys.argv[1]

        print(f"The text contains {len(s)} characters:")
        print(f"{sum(c.isupper() for c in s)} upper letters")
        print(f"{sum(c.islower() for c in s)} lower letters")
        print(f"{sum(c in string.punctuation for c in s)} punctuation marks")
        print(f"{sum(c.isspace() for c in s)} spaces")
        print(f"{sum(c.isdigit() for c in s)} digits")
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
