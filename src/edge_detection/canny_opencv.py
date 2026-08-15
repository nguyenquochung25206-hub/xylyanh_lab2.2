import cv2

from src.preprocessing.grayscale import convert_to_grayscale
from src.preprocessing.gaussian_blur import apply_gaussian_blur


def detect_edges(
    image,
    low_threshold=100,
    high_threshold=200,
    sigma=1.0
):
    """
    Detect edges using OpenCV Canny.

    Pipeline:

        Input Image
            |
            v
        Grayscale
            |
            v
        Gaussian Blur
            |
            v
        Canny
            |
            v
        Edge Image

    Parameters:
        image:
            Input BGR image.

        low_threshold:
            Lower threshold of Canny.

        high_threshold:
            Higher threshold of Canny.

        sigma:
            Sigma value used by Gaussian Blur.

    Returns:
        Binary edge image.
    """

    # Step 1: Convert image to grayscale.
    gray = convert_to_grayscale(image)

    # Step 2: Reduce noise using Gaussian Blur.
    blurred = apply_gaussian_blur(
        gray,
        kernel_size=(5, 5),
        sigma=sigma
    )

    # Step 3: Detect edges using OpenCV Canny.
    edges = cv2.Canny(
        blurred,
        low_threshold,
        high_threshold
    )

    # Return detected edges.
    return edges
