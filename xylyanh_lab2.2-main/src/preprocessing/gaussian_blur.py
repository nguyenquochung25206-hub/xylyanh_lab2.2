import cv2


def apply_gaussian_blur(
    image,
    kernel_size=(5, 5),
    sigma=1.0
):
    """
    Apply Gaussian Blur to reduce image noise.

    Parameters:
        image:
            Input image.

        kernel_size:
            Size of Gaussian kernel.

        sigma:
            Sigma value of Gaussian filter.

    Returns:
        Blurred image.
    """

    # Apply Gaussian Blur.
    blurred = cv2.GaussianBlur(
        image,
        kernel_size,
        sigma
    )

    # Return blurred image.
    return blurred