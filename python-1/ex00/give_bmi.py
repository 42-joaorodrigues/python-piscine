import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """Return the BMI for each height/weight pair."""
    try:
        if not isinstance(height, list) or not isinstance(weight, list):
            raise TypeError("height and weight must be lists")
        for v in height + weight:
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise TypeError("values must be int or float")
            if v <= 0:
                raise ValueError("values must be positive")
        if len(height) != len(weight):
            raise ValueError("height and weight must have the same size")
        h = np.array(height)
        w = np.array(weight)
        return (w / h**2).tolist()
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True for each BMI above the limit, False otherwise."""
    try:
        if not isinstance(bmi, list):
            raise TypeError("bmi must be a list")
        for v in bmi:
            if isinstance(v, bool) or not isinstance(v, (int, float)):
                raise TypeError("values must be int or float")
        if isinstance(limit, bool) or not isinstance(limit, int):
            raise TypeError("limit must be an int")
        return (np.array(bmi) > limit).tolist()
    except TypeError as e:
        print(f"Error: {e}")
        return []


def main():
    """Run a quick test of give_bmi and apply_limit."""
    bmi = give_bmi([2.71, 1.15], [165.3, 38.4])
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
