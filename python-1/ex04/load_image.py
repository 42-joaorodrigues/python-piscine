import sys

import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    """Load an image, print its shape and return its RGB pixels."""
    try:
        if not isinstance(path, str):
            raise TypeError("path must be a string")
        with Image.open(path) as img:
            rgb = img.convert("RGB")
    except (OSError, TypeError) as e:
        print(f"Error: {e}")
        return np.array([])
    arr = np.array(rgb)
    print(f"The shape of image is: {arr.shape}")
    return arr


def main():
    """Load the image given as argument and print its pixels."""
    if len(sys.argv) != 2:
        print("Usage: python load_image.py <image_path>")
        return
    print(ft_load(sys.argv[1]))


if __name__ == "__main__":
    main()
