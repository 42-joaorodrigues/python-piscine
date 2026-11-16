import io
from contextlib import redirect_stdout

from NULL_not_found import NULL_not_found

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False

NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))


def check(value, expected, expected_ret):
    """Run NULL_not_found(value), print its output and OK/KO."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        ret = NULL_not_found(value)
    out = buf.getvalue()
    ok = out == expected + "\n" and ret == expected_ret
    print(f"{value!r:14} {out.rstrip(chr(10))!r:40} "
          f"return {ret!r} -> {'OK' if ok else 'KO'}")
    if not ok:
        print(f"    expected {expected!r} return {expected_ret}")


print("--- checks ---")
# subject
check(Nothing, "Nothing: None <class 'NoneType'>", 0)
check(Garlic, "Cheese: nan <class 'float'>", 0)
check(Zero, "Zero: 0 <class 'int'>", 0)
check(Empty, "Empty: <class 'str'>", 0)
check(Fake, "Fake: False <class 'bool'>", 0)
check("Brian", "Type not Found", 1)
# right type, wrong value
check(5, "Type not Found", 1)
check(3.5, "Type not Found", 1)
check(float("inf"), "Type not Found", 1)
check(" ", "Type not Found", 1)
check(True, "Type not Found", 1)
# falsy values of other types
check(0.0, "Type not Found", 1)
check(0j, "Type not Found", 1)
check([], "Type not Found", 1)
check({}, "Type not Found", 1)
check(b"", "Type not Found", 1)
