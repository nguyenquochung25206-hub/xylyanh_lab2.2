import cv2
import pytest

from src.edge_detection.canny_opencv import detect_edges


IMAGE_PATHS = [
    "data/input/normal/panda_normal.png",
    "data/input/noisy/panda_noisy.png",
    "data/input/low_contrast/panda_low_contrast.png",
    "data/input/high_contrast/panda_high_contrast.png",
]


@pytest.mark.parametrize("image_path", IMAGE_PATHS)
def test_canny(image_path):
    # Read input image
    image = cv2.imread(image_path)

    # Check that image was loaded successfully
    assert image is not None, f"Cannot read image: {image_path}"

    # Detect edges
    edges = detect_edges(
        image,
        low_threshold=100,
        high_threshold=200,
        sigma=1.0
    )

    # Check output is not None
    assert edges is not None

    # Canny output must be a single-channel image
    assert len(edges.shape) == 2

    # Edge image must have the same height and width as input
    assert edges.shape == image.shape[:2]

    # Canny output should contain at least some detected edges
    assert cv2.countNonZero(edges) > 0

    # Save output image
    output_path = f"tv3/output/canny/canny_{image_path}"
    success = cv2.imwrite(output_path, edges)

    # Check that output image was saved successfully
    assert success
