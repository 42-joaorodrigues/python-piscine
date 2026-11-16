from typing import Any


def NULL_not_found(object: Any) -> int:
    obj_type = type(object)

    if object is None:
        print("Nothing:", object, obj_type)
    elif obj_type is float and object != object:
        print("Cheese:", object, obj_type)
    elif obj_type is int and object == 0:
        print("Zero:", object, obj_type)
    elif obj_type is str and len(object) == 0:
        print("Empty:", obj_type)
    elif object is False:
        print("Fake:", object, obj_type)
    else:
        print("Type not Found")
        return 1

    return 0
