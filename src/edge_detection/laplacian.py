import cv2

from src.preprocessing.grayscale import convert_to_grayscale
from src.preprocessing.gaussian_blur import apply_gaussian_blur


def detect_edges(
    image,
    kernel_size=3,
    sigma=1.0
):
    """
    Detect edges using the Laplacian algorithm.

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
        Laplacian
            |
            v
        Edge Image

    Parameters:
        image:
            Input BGR image.

        kernel_size:
            Kernel size used by Laplacian.

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

    # Step 3: Detect edges using Laplacian
    laplacian = cv2.Laplacian(
        blurred,
        cv2.CV_64F,
        ksize=kernel_size
    )

    # Convert result to 8-bit image
    edges = cv2.convertScaleAbs(laplacian)

    return edges
