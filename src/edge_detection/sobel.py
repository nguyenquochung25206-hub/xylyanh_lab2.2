import cv2

from src.preprocessing.grayscale import convert_to_grayscale
from src.preprocessing.gaussian_blur import apply_gaussian_blur


def detect_edges(
    image,
    kernel_size=3,
    sigma=1.0
):
    """
    Detect edges using the Sobel algorithm.

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
        Sobel X and Sobel Y
            |
            v
        Edge Image

    Parameters:
        image:
            Input BGR image.

        kernel_size:
            Kernel size used by Sobel.

        sigma:
            Sigma value used by Gaussian Blur.

    Returns:
        8-bit edge image.
    """

    # Step 1: Convert image to grayscale
    gray = convert_to_grayscale(image)

    # Step 2: Reduce noise using Gaussian Blur
    blurred = apply_gaussian_blur(
        gray,
        kernel_size=(5, 5),
        sigma=sigma
    )

    # Step 3: Detect horizontal edges
    sobel_x = cv2.Sobel(
        blurred,
        cv2.CV_64F,
        1,
        0,
        ksize=kernel_size
    )

    # Step 4: Detect vertical edges
    sobel_y = cv2.Sobel(
        blurred,
        cv2.CV_64F,
        0,
        1,
        ksize=kernel_size
    )

    # Step 5: Combine horizontal and vertical edges
    magnitude = cv2.magnitude(sobel_x, sobel_y)

    # Convert result to 8-bit image
    edges = cv2.convertScaleAbs(magnitude)

    return edges
