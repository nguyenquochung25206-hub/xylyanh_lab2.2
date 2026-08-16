import cv2


def convert_to_grayscale(image):
    """
    Convert a color image to grayscale.

    Parameters:
        image: Input BGR image.

    Returns:
        Grayscale image.
    """

    # Convert BGR image to grayscale.
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Return grayscale image.
    return gray