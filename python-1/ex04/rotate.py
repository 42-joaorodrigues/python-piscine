import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def ft_transpose(array: np.ndarray) -> np.ndarray:
    """Return the transpose of a 2D array, computed by hand."""
    rows = len(array)
    cols = len(array[0])
    result = [[array[r][c] for r in range(rows)] for c in range(cols)]
    return np.array(result)


def main():
    """Load animal.jpeg, cut a square, transpose it and display it."""
    img = ft_load("../assets/animal.jpeg")
    if img.size == 0:
        return
    square = img[100:500, 450:850, 0]
    print(f"The shape of image is: {square.shape}")
    print(square)
    try:
        rotated = ft_transpose(square)
        print(f"New shape after Transpose: {rotated.shape}")
        print(rotated)
        plt.imshow(rotated, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
