import matplotlib.pyplot as plt
import numpy as np

from load_image import ft_load


def check(array: np.ndarray) -> None:
    """Raise TypeError if array is not an RGB image of shape (h, w, 3)."""
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a numpy array")
    if array.ndim != 3 or array.shape[2] != 3:
        raise TypeError("array must have shape (height, width, 3)")


def show(array: np.ndarray) -> None:
    """Display an image array in a window, without axes."""
    plt.imshow(array)
    plt.axis("off")
    plt.show()


def apply(array: np.ndarray, transform) -> np.ndarray:
    """Check array, apply transform to it, display and return the result."""
    try:
        check(array)
        result = transform(array)
        show(result)
        return result
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    return apply(array, lambda a: 255 - a)


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image received."""
    return apply(array, lambda a: a * np.array([1, 0, 0], dtype=np.uint8))


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel of the image received."""
    def transform(a: np.ndarray) -> np.ndarray:
        """Return a copy of a with red and blue set to zero."""
        green = a.copy()
        green[:, :, 0] = green[:, :, 0] - green[:, :, 0]
        green[:, :, 2] = green[:, :, 2] - green[:, :, 2]
        return green
    return apply(array, transform)


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel of the image received."""
    def transform(a: np.ndarray) -> np.ndarray:
        """Return a copy of a with red and green set to zero."""
        blue = a.copy()
        blue[:, :, 0:2] = 0
        return blue
    return apply(array, transform)


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Turns the image received into shades of grey."""
    def transform(a: np.ndarray) -> np.ndarray:
        """Return a copy of a where each channel is the pixel's mean."""
        grey = a.copy()
        mean = a.sum(axis=2) / 3
        grey[:, :, 0] = mean
        grey[:, :, 1] = mean
        grey[:, :, 2] = mean
        return grey
    return apply(array, transform)


def main():
    """Load landscape.jpg and apply each filter."""
    array = ft_load("../assets/landscape.jpg")
    if array.size == 0:
        return
    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)


if __name__ == "__main__":
    main()
