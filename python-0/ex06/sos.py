import sys


def encode(text: str) -> str:
    """Return text encoded in Morse code."""
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
        "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
        "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. ",
    }
    try:
        return "".join(NESTED_MORSE[c] for c in text.upper()).rstrip()
    except KeyError:
        raise AssertionError("the arguments are bad")


def main():
    """Encode the argument in Morse code."""
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        print(encode(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
