import matplotlib.pyplot as plt

from load_image import ft_load


def main():
    """Load animal.jpeg, zoom on it and display the result."""
    img = ft_load("../assets/animal.jpeg")
    if img.size == 0:
        return
    print(img)
    try:
        zoom = img[100:500, 450:850, 0:1]
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)
        plt.imshow(zoom[:, :, 0], cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
