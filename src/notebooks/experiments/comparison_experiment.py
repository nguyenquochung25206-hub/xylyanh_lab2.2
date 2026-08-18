import cv2
from pathlib import Path

from src.edge_detection.canny_opencv import (
    detect_edges as detect_canny
)

from src.edge_detection.sobel import (
    detect_edges as detect_sobel
)

from src.edge_detection.laplacian import (
    detect_edges as detect_laplacian
)


def compare_edges(
    image,
    low_threshold=100,
    high_threshold=200,
    kernel_size=3,
    sigma=1.0
):
    """
    Compare Canny, Sobel and Laplacian.

    Pipeline:
        Input Image
            |
            v
        Canny - Sobel - Laplacian
            |
            v
        Comparison Image

    Parameters:
        image:
            Input BGR image.

        low_threshold:
            Lower threshold of Canny.

        high_threshold:
            Higher threshold of Canny.

        kernel_size:
            Kernel size of Sobel and Laplacian.

        sigma:
            Sigma value used by Gaussian Blur.

    Returns:
        Combined comparison image.
    """

    # Step 1: Detect edges using Canny
    canny_result = detect_canny(
        image,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
        sigma=sigma
    )

    # Step 2: Detect edges using Sobel
    sobel_result = detect_sobel(
        image,
        kernel_size=kernel_size,
        sigma=sigma
    )

    # Step 3: Detect edges using Laplacian
    laplacian_result = detect_laplacian(
        image,
        kernel_size=kernel_size,
        sigma=sigma
    )

    # Step 4: Convert edge images to BGR
    canny_result = cv2.cvtColor(
        canny_result,
        cv2.COLOR_GRAY2BGR
    )

    sobel_result = cv2.cvtColor(
        sobel_result,
        cv2.COLOR_GRAY2BGR
    )

    laplacian_result = cv2.cvtColor(
        laplacian_result,
        cv2.COLOR_GRAY2BGR
    )

    # Step 5: Combine the results
    comparison = cv2.hconcat([
        image,
        canny_result,
        sobel_result,
        laplacian_result
    ])

    return comparison


def run_experiment():
    """Run comparison on different image types."""

    image_paths = {
        "normal": "data/input/normal/sample.png",
        "noisy": "data/input/noisy/sample_noisy.png",
        "low_contrast":
            "data/input/low_contrast/sample_low_contrast.png",
        "high_contrast":
            "data/input/high_contrast/sample_high_contrast.png"
    }

    output_folder = Path("data/output/comparison")
    output_folder.mkdir(parents=True, exist_ok=True)

    for image_name, image_path in image_paths.items():

        image = cv2.imread(image_path)

        if image is None:
            print("Cannot read image:", image_path)
            continue

        comparison = compare_edges(image)

        output_path = (
            output_folder
            / f"{image_name}_comparison.png"
        )

        cv2.imwrite(
            str(output_path),
            comparison
        )

        print("Saved:", output_path)


if __name__ == "__main__":
    run_experiment()
