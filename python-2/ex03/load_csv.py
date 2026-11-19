import sys

import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file, print its dimensions and return it (None on error)."""
    try:
        if not isinstance(path, str) or not path.endswith(".csv"):
            raise ValueError("path must be a .csv file path")
        df = pd.read_csv(path)
    except (OSError, ValueError) as e:
        print(f"Error: {e}")
        return None
    print(f"Loading dataset of dimensions {df.shape}")
    return df


def main():
    """Load the CSV given as argument and print it."""
    if len(sys.argv) != 2:
        print("Usage: python load_csv.py <file.csv>")
        return
    print(load(sys.argv[1]))


if __name__ == "__main__":
    main()
