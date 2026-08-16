import csv
import numpy as np
import pytest

from src.experiments.parameter_experiment import (
    create_sample_image,
    load_input_image,
    compute_edge_density,
    run_sigma_experiment,
    run_threshold_experiment,
    run_experiment,
)


# 1. Test tạo ảnh mẫu
def test_create_sample_image():
    img = create_sample_image(100, 100)

    assert img.shape == (100, 100, 3)
    assert img.dtype == np.uint8


# 2. Test load ảnh không tồn tại
def test_load_input_image_not_found():
    with pytest.raises(FileNotFoundError):
        load_input_image("invalid_path.jpg")


# 3. Test edge density
@pytest.mark.parametrize(
    "white_count, total, expected",
    [
        (0, 100, 0.0),
        (50, 100, 50.0),
        (100, 100, 100.0),
    ]
)
def test_compute_edge_density(
    white_count,
    total,
    expected
):
    edges = np.zeros(total, dtype=np.uint8)
    edges[:white_count] = 255

    assert compute_edge_density(edges) == expected


# 4. Test Sigma + Threshold
# TC07 - kt Sigma
def test_sigma_experiment():

    img = create_sample_image(200, 200)

    results = run_sigma_experiment(
        img,
        sigma_values=[0.5, 1.0, 1.5]
    )

    assert len(results) == 3

    for result in results:
        assert "sigma" in result
        assert "edge_density_percent" in result
        assert "processing_time_ms" in result
        assert "edges" in result

        assert result["edges"].shape == (200, 200)


# TC08 - Kt Threshold
def test_threshold_experiment():

    img = create_sample_image(200, 200)

    results = run_threshold_experiment(
        img,
        threshold_pairs=[
            (50, 100),
            (100, 200),
            (150, 300)
        ]
    )

    assert len(results) == 3

    for result in results:
        assert "low_threshold" in result
        assert "high_threshold" in result
        assert "edge_density_percent" in result
        assert "processing_time_ms" in result
        assert "edges" in result

        assert result["edges"].shape == (200, 200)


# 5. Test toàn bộ pipeline
def test_run_experiment(tmp_path, monkeypatch):

    monkeypatch.setattr(
        "src.experiments.parameter_experiment.FIGURES_DIR",
        tmp_path / "figures"
    )

    monkeypatch.setattr(
        "src.experiments.parameter_experiment.TABLES_DIR",
        tmp_path / "tables"
    )

    output = run_experiment(
        sigma_values=[0.5, 1.0],
        threshold_pairs=[(50, 100)]
    )

    assert output["sigma_figure"].exists()
    assert output["threshold_figure"].exists()
    assert output["table"].exists()

    with open(
        output["table"],
        encoding="utf-8",
        newline=""
    ) as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 3
