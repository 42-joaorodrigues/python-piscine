import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print the shape of a 2D list, slice its rows and return them."""
    try:
        if not isinstance(family, list):
            raise TypeError("family must be a list")
        for row in family:
            if not isinstance(row, list):
                raise TypeError("each row must be a list")
            if len(row) != len(family[0]):
                raise ValueError("all rows must have the same size")
        arr = np.array(family)
        if arr.ndim != 2:
            raise ValueError("family must be a 2D array")
        print(f"My shape is : {arr.shape}")
        new = family[start:end]
        print(f"My new shape is : {np.array(new).shape}")
        return new
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return []


def main():
    """Entry point, tests go here."""
    family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
