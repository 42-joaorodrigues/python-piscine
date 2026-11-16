from typing import Any


def all_thing_is_obj(object: Any) -> int:
    obj_type = type(object)

    if isinstance(object, (list, tuple, set, dict)):
        print(obj_type.__name__.capitalize(), ":", obj_type)
    elif isinstance(object, str):
        print(object, "is in the kitchen :", obj_type)
    else:
        print("Type not found")
    return 42
