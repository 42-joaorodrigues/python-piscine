import sys


def main():
    try:
        if len(sys.argv) < 2:
            return

        assert len(sys.argv) == 2, "more than one argument is provided"

        try:
            nbr = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if nbr % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
