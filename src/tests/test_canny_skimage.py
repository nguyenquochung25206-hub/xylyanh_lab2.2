import cv2
import pytest

from src.edge_detection.canny_skimage import canny_skimage


IMAGE_PATHS = [
    "data/input/normal/panda_normal.png",
    "data/input/noisy/panda_noisy.png",
    "data/input/low_contrast/panda_low_contrast.png",
    "data/input/high_contrast/panda_high_contrast.png",
]


@pytest.mark.parametrize("image_path", IMAGE_PATHS)
def test_canny_skimage(image_path):
    image = cv2.imread(image_path)

    assert image is not None, f"Cannot read image: {image_path}"

    edges = canny_skimage(
        image,
        sigma=1.0,
        low_threshold=100,
        high_threshold=200
    )

    assert edges is not None

    # Output phải là ảnh 2 chiều
    assert len(edges.shape) == 2

    # Kích thước output phải bằng ảnh input
    assert edges.shape == image.shape[:2]

    # Output phải là uint8
    assert edges.dtype == "uint8"

    # Giá trị pixel chỉ được là 0 hoặc 255
    assert set(edges.flatten()).issubset({0, 255})
