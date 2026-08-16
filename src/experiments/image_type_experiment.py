from pathlib import Path
import cv2
import numpy as np


def create_image_types(image):
    """
    Create noisy, low-contrast and high-contrast images.

    Parameters:
        image:
            Input BGR image.

    Returns:
        Three processed BGR images.
    """

    # Step 1: Create noisy image
    noise = np.random.normal(
        0,
        25,
        image.shape
    )

    noisy = np.clip(
        image.astype(np.float32) + noise,
        0,
        255
    ).astype(np.uint8)

    # Step 2: Create low-contrast image
    low_contrast = cv2.convertScaleAbs(
        image,
        alpha=0.5,
        beta=60
    )

    # Step 3: Create high-contrast image
    high_contrast = cv2.convertScaleAbs(
        image,
        alpha=1.8,
        beta=0
    )

    return noisy, low_contrast, high_contrast


def run_experiment():
    """Read a BGR image and create different image types."""

    project_folder = Path(__file__).resolve().parents[2]
    normal_folder = project_folder / "data/input/normal"

    # Find the first image in the normal folder
    image_files = [
        file
        for file in normal_folder.iterdir()
        if file.suffix.lower() in (".png", ".jpg", ".jpeg")
    ]

    if not image_files:
        print("No image found in:", normal_folder)
        return

    input_path = image_files[0]

    # cv2.imread reads the image in BGR format
    image = cv2.imread(
        str(input_path),
        cv2.IMREAD_COLOR
    )

    if image is None:
        print("Cannot read image:", input_path)
        return

    noisy, low_contrast, high_contrast = (
        create_image_types(image)
    )

    image_name = input_path.stem

    output_paths = {
        "noisy":
            project_folder
            / f"data/input/noisy/{image_name}_noisy.png",

        "low_contrast":
            project_folder
            / (
                "data/input/low_contrast/"
                f"{image_name}_low_contrast.png"
            ),

        "high_contrast":
            project_folder
            / (
                "data/input/high_contrast/"
                f"{image_name}_high_contrast.png"
            )
    }

    cv2.imwrite(
        str(output_paths["noisy"]),
        noisy
    )

    cv2.imwrite(
        str(output_paths["low_contrast"]),
        low_contrast
    )

    cv2.imwrite(
        str(output_paths["high_contrast"]),
        high_contrast
    )

    print("Created noisy image")
    print("Created low-contrast image")
    print("Created high-contrast image")


if __name__ == "__main__":
    run_experiment()
