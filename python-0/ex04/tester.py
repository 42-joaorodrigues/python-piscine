import subprocess
import sys

# (arguments, expected output)
CASES = [
    # subject
    (["14"], "I'm Even.\n"),
    (["-5"], "I'm Odd.\n"),
    ([], ""),
    (["0"], "I'm Even.\n"),
    (["Hi!"], "AssertionError: argument is not an integer\n"),
    (["13", "5"], "AssertionError: more than one argument is provided\n"),
    # extra
    (["+3"], "I'm Odd.\n"),
    (["-0"], "I'm Even.\n"),
    (["99999999999999999999"], "I'm Odd.\n"),
    (["3.0"], "AssertionError: argument is not an integer\n"),
    ([""], "AssertionError: argument is not an integer\n"),
    (["1 2"], "AssertionError: argument is not an integer\n"),
    (["1", "2", "3"], "AssertionError: more than one argument is provided\n"),
]


def main():
    """Run whatis.py with each case and print OK/KO."""
    for args, expected in CASES:
        result = subprocess.run([sys.executable, "whatis.py"] + args,
                                capture_output=True, text=True)
        out = result.stdout + result.stderr
        status = "OK" if out == expected else "KO"
        print(f"{str(args):28} {out.rstrip()!r:55} -> {status}")
        if status == "KO":
            print(f"    expected {expected.rstrip()!r}")


if __name__ == "__main__":
    main()
