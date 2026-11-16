import io
from contextlib import redirect_stdout

from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))


def check(value, expected):
    """Run all_thing_is_obj(value), print its output and OK/KO."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        ret = all_thing_is_obj(value)
    out = buf.getvalue()
    ok = out == expected + "\n" and ret == 42
    print(f"{out.rstrip(chr(10))!r:50} -> {'OK' if ok else 'KO'}")
    if not ok:
        print(f"    expected {expected!r} return 42, got return {ret!r}")


print("--- checks ---")
# subject
check(ft_list, "List : <class 'list'>")
check(ft_tuple, "Tuple : <class 'tuple'>")
check(ft_set, "Set : <class 'set'>")
check(ft_dict, "Dict : <class 'dict'>")
check("Brian", "Brian is in the kitchen : <class 'str'>")
check("Toto", "Toto is in the kitchen : <class 'str'>")
check(10, "Type not found")
# empty containers and string
check([], "List : <class 'list'>")
check((), "Tuple : <class 'tuple'>")
check(set(), "Set : <class 'set'>")
check({}, "Dict : <class 'dict'>")
check("", " is in the kitchen : <class 'str'>")
# other types
check(None, "Type not found")
check(3.5, "Type not found")
check(True, "Type not found")
check(frozenset(), "Type not found")
check(b"bytes", "Type not found")
