import cv2
import numpy as np

from src.edge_detection.canny_opencv import detect_edges
from src.edge_detection.canny_skimage import canny_skimage

from src.experiments.parameter_experiment import (
    run_sigma_experiment,
    run_threshold_experiment
)


def load_test_image():
    """
    Load a normal input image for pipeline testing.
    """

    image_path = "data/input/normal/panda_normal.png"

    image = cv2.imread(image_path)

    assert image is not None, (
        f"Cannot read test image: {image_path}"
    )

    return image


def test_canny_opencv_pipeline():
    """
    Test the complete OpenCV Canny pipeline:

    Input
        ↓
    Grayscale
        ↓
    Gaussian Blur
        ↓
    Canny OpenCV
        ↓
    Edge Image
    """

    image = load_test_image()

    edges = detect_edges(
        image,
        low_threshold=100,
        high_threshold=200,
        sigma=1.0
    )

    # Output must exist
    assert edges is not None

    # Output must be a 2D grayscale image
    assert len(edges.shape) == 2

    # Output size must match input image
    assert edges.shape[:2] == image.shape[:2]

    # Canny output must be uint8
    assert edges.dtype == np.uint8

    # Output must contain edge information
    assert np.count_nonzero(edges) > 0


def test_canny_skimage_pipeline():
    """
    Test the Scikit-image Canny pipeline.

    Input
        ↓
    Grayscale conversion
        ↓
    Scikit-image Canny
        ↓
    Edge Image
    """

    image = load_test_image()

    # OpenCV loads image as BGR.
    # Scikit-image expects RGB.
    image_rgb = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    edges = canny_skimage(
        image_rgb,
        sigma=1.0
    )

    # Output must exist
    assert edges is not None

    # Output must be a 2D image
    assert len(edges.shape) == 2

    # Output size must match input image
    assert edges.shape == image.shape[:2]

    # Output must be uint8
    assert edges.dtype == np.uint8

    # Output must contain edge information
    assert np.count_nonzero(edges) > 0


def test_parameter_pipeline():
    """
    Test the complete parameter experiment pipeline.

    Input
        ↓
    Canny OpenCV
        ↓
    Sigma Experiment
        +
    Threshold Experiment
        ↓
    Experiment Results
    """

    image = load_test_image()

    # Test Sigma experiment
    sigma_values = [
        0.5,
        1.0,
        1.5
    ]

    sigma_results = run_sigma_experiment(
        image,
        sigma_values=sigma_values,
        low_threshold=100,
        high_threshold=200
    )

    # Number of results must match number of Sigma values
    assert len(sigma_results) == len(sigma_values)

    for result in sigma_results:

        # Required result information
        assert "sigma" in result
        assert "low_threshold" in result
        assert "high_threshold" in result
        assert "edge_density_percent" in result
        assert "processing_time_ms" in result
        assert "edges" in result

        # Edge image must exist
        assert result["edges"] is not None

        # Edge image must have correct size
        assert result["edges"].shape == image.shape[:2]

        # Edge image must be uint8
        assert result["edges"].dtype == np.uint8

        # Density must be valid
        assert 0 <= result["edge_density_percent"] <= 100

        # Processing time must be positive
        assert result["processing_time_ms"] >= 0

    # Test Threshold experiment
    threshold_pairs = [
        (50, 100),
        (100, 200),
        (150, 300)
    ]

    threshold_results = run_threshold_experiment(
        image,
        threshold_pairs=threshold_pairs,
        sigma=1.0
    )

    # Number of results must match number of threshold pairs
    assert len(threshold_results) == len(threshold_pairs)

    for result in threshold_results:

        assert "sigma" in result
        assert "low_threshold" in result
        assert "high_threshold" in result
        assert "edge_density_percent" in result
        assert "processing_time_ms" in result
        assert "edges" in result

        # Check output
        assert result["edges"] is not None
        assert result["edges"].shape == image.shape[:2]
        assert result["edges"].dtype == np.uint8

        # Check measured values
        assert 0 <= result["edge_density_percent"] <= 100
        assert result["processing_time_ms"] >= 0
