import cv2
import matplotlib.pyplot as plt


def plot_comparison(
    image,
    canny_result,
    sobel_result,
    laplacian_result
):
    """
    Plot the original image and edge detection results.

    Parameters:
        image:
            Original BGR image.

        canny_result:
            Edge image produced by Canny.

        sobel_result:
            Edge image produced by Sobel.

        laplacian_result:
            Edge image produced by Laplacian.

    Returns:
        Matplotlib figure.
    """

    # Convert the original BGR image to RGB
    original_rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    titles = [
        "Original",
        "Canny",
        "Sobel",
        "Laplacian"
    ]

    results = [
        original_rgb,
        canny_result,
        sobel_result,
        laplacian_result
    ]

    # Create four comparison plots
    figure, axes = plt.subplots(
        1,
        4,
        figsize=(16, 5)
    )

    for index in range(4):
        if index == 0:
            axes[index].imshow(results[index])
        else:
            axes[index].imshow(
                results[index],
                cmap="gray"
            )

        axes[index].set_title(titles[index])
        axes[index].axis("off")

    figure.tight_layout()

    return figure
