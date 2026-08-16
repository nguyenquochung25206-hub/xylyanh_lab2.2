"""
Parameter Experiment Module (TV5)
==================================

Muc tieu:
    Thay doi cac tham so cua Canny Edge Detection (Sigma cua Gaussian
    Blur, Low Threshold, High Threshold) va quan sat anh huong cua
    chung den ket qua phat hien bien.

Pipeline:

    Input Image
        |
        v
    Canny OpenCV (detect_edges)
        |
        +--> Thi nghiem 1: Thay doi Sigma (giu Threshold co dinh)
        |
        +--> Thi nghiem 2: Thay doi Threshold (giu Sigma co dinh)
        |
        v
    Ket qua:
        - results/figures/sigma_comparison.png
        - results/figures/threshold_comparison.png
        - results/tables/parameter_results.csv

Ghi chu:
    Module nay tai su dung ham `detect_edges()` do TV3 cung cap trong
    `src/edge_detection/canny_opencv.py`. Ham nay da bao goc toan bo
    pipeline (Grayscale -> Gaussian Blur -> Canny) nen TV5 chi can goi
    voi cac gia tri tham so khac nhau va do luong ket qua.
"""

import csv
import time
from pathlib import Path

import cv2
import numpy as np

import matplotlib
matplotlib.use("Agg")  # Khong can hien thi man hinh (GUI) khi chay script
import matplotlib.pyplot as plt

from src.edge_detection.canny_opencv import detect_edges


# ---------------------------------------------------------------------------
# Cau hinh mac dinh
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_DIR = PROJECT_ROOT / "data" / "input" / "normal"
FIGURES_DIR = PROJECT_ROOT / "results" / "figures"
TABLES_DIR = PROJECT_ROOT / "results" / "tables"

# EXP-01: Danh sach gia tri Sigma can thu nghiem.
DEFAULT_SIGMA_VALUES = [0.5, 1.0, 1.5, 2.0, 3.0]

# EXP-02: Danh sach cap (low_threshold, high_threshold) can thu nghiem.
DEFAULT_THRESHOLD_PAIRS = [
    (50, 100),
    (50, 150),
    (100, 200),
    (100, 250),
    (150, 300),
]

# Gia tri co dinh dung lam baseline khi thay doi tham so con lai.
DEFAULT_SIGMA = 1.0
DEFAULT_LOW_THRESHOLD = 100
DEFAULT_HIGH_THRESHOLD = 200


# ---------------------------------------------------------------------------
# Chuan bi anh dau vao
# ---------------------------------------------------------------------------

def create_sample_image(width=400, height=400):
    """
    Tao mot anh mau tong hop (synthetic) gom cac hinh khoi co ban.

    Ham nay chi duoc su dung khi trong `data/input/normal/` chua co
    anh that nao, de dam bao pipeline thi nghiem luon co the chay duoc
    ma khong bi loi thieu du lieu dau vao.

    Parameters:
        width, height:
            Kich thuoc anh can tao.

    Returns:
        Anh BGR (numpy array) chua hinh chu nhat, hinh tron, duong
        thang va mot it nhieu (noise) nhe de mo phong anh thuc te.
    """

    # Nen mau xam trung tinh.
    image = np.full((height, width, 3), 200, dtype=np.uint8)

    # Hinh chu nhat lon.
    cv2.rectangle(
        image,
        (40, 40),
        (200, 180),
        (40, 40, 40),
        thickness=-1
    )

    # Hinh tron.
    cv2.circle(
        image,
        (300, 120),
        70,
        (90, 160, 90),
        thickness=-1
    )

    # Hinh tam giac (dung polylines).
    triangle = np.array([[80, 350], [200, 230], [320, 350]])
    cv2.fillPoly(image, [triangle], (60, 90, 200))

    # Vai duong thang de tao them bien ro net.
    cv2.line(image, (0, 250), (400, 250), (20, 20, 20), 2)
    cv2.line(image, (200, 0), (200, 400), (20, 20, 20), 1)

    # Them nhieu Gaussian nhe de anh gan voi thuc te hon.
    # Dung seed co dinh de ket qua thi nghiem co the tai lap
    # (reproducible) giua cac lan chay.
    rng = np.random.default_rng(seed=42)
    noise = rng.normal(0, 8, image.shape)
    noisy_image = np.clip(
        image.astype(np.float32) + noise,
        0,
        255
    ).astype(np.uint8)

    return noisy_image


def load_input_image(input_path=None):
    """
    Nap anh dau vao cho thi nghiem.

    Thu tu uu tien:
        1. Duong dan `input_path` do nguoi dung chi dinh (neu co).
        2. Anh dau tien tim thay trong `data/input/normal/`.
        3. Neu khong co anh nao, tu dong tao anh mau tong hop va
           luu lai vao `data/input/normal/` de cac lan chay sau
           co the tai su dung.

    Parameters:
        input_path:
            Duong dan anh cu the (str hoac Path). Co the la None.

    Returns:
        (image, image_name): Anh BGR va ten anh (khong bao gom duoi file).
    """

    if input_path is not None:
        image = cv2.imread(str(input_path))
        if image is None:
            raise FileNotFoundError(
                f"Khong doc duoc anh: {input_path}"
            )
        return image, Path(input_path).stem

    INPUT_DIR.mkdir(parents=True, exist_ok=True)

    candidates = sorted(
        file for file in INPUT_DIR.iterdir()
        if file.suffix.lower() in (".png", ".jpg", ".jpeg", ".bmp")
    )

    if candidates:
        chosen = candidates[0]
        image = cv2.imread(str(chosen))
        if image is not None:
            return image, chosen.stem

    print(
        "[INFO] Khong tim thay anh trong data/input/normal/. "
        "Tu dong tao anh mau tong hop de chay thi nghiem."
    )

    image = create_sample_image()
    sample_path = INPUT_DIR / "sample_generated.jpg"
    cv2.imwrite(str(sample_path), image)
    print(f"[INFO] Da luu anh mau tai: {sample_path}")

    return image, "sample_generated"


# ---------------------------------------------------------------------------
# Do luong ket qua
# ---------------------------------------------------------------------------

def compute_edge_density(edges):
    """
    Tinh mat do bien (edge density) cua anh nhi phan.

    Parameters:
        edges:
            Anh bien nhi phan (0 hoac 255) tra ve tu Canny.

    Returns:
        Ty le phan tram pixel bien tren tong so pixel.
    """

    white_pixels = np.count_nonzero(edges)
    total_pixels = edges.size
    return (white_pixels / total_pixels) * 100.0


# ---------------------------------------------------------------------------
# Thi nghiem 1: Sigma
# ---------------------------------------------------------------------------

def run_sigma_experiment(
    image,
    sigma_values=None,
    low_threshold=DEFAULT_LOW_THRESHOLD,
    high_threshold=DEFAULT_HIGH_THRESHOLD
):
    """
    EXP-01: Chay Canny voi nhieu gia tri Sigma khac nhau, giu nguyen
    Low/High Threshold, de quan sat anh huong cua Gaussian Blur den
    ket qua phat hien bien.

    Parameters:
        image:
            Anh BGR dau vao.

        sigma_values:
            Danh sach cac gia tri sigma can thu nghiem.

        low_threshold, high_threshold:
            Gia tri threshold co dinh dung lam baseline.

    Returns:
        Danh sach dict, moi phan tu gom:
            sigma, low_threshold, high_threshold,
            edge_density_percent, processing_time_ms, edges
    """

    sigma_values = sigma_values or DEFAULT_SIGMA_VALUES
    results = []

    for sigma in sigma_values:
        start_time = time.perf_counter()

        edges = detect_edges(
            image,
            low_threshold=low_threshold,
            high_threshold=high_threshold,
            sigma=sigma
        )

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        results.append({
            "sigma": sigma,
            "low_threshold": low_threshold,
            "high_threshold": high_threshold,
            "edge_density_percent": round(
                compute_edge_density(edges), 3
            ),
            "processing_time_ms": round(elapsed_ms, 3),
            "edges": edges
        })

    return results


# ---------------------------------------------------------------------------
# Thi nghiem 2: Threshold
# ---------------------------------------------------------------------------

def run_threshold_experiment(
    image,
    threshold_pairs=None,
    sigma=DEFAULT_SIGMA
):
    """
    EXP-02: Chay Canny voi nhieu cap (Low, High) Threshold khac nhau,
    giu nguyen Sigma, de quan sat anh huong cua Threshold den ket
    qua phat hien bien.

    Parameters:
        image:
            Anh BGR dau vao.

        threshold_pairs:
            Danh sach cac cap (low_threshold, high_threshold).

        sigma:
            Gia tri sigma co dinh dung lam baseline.

    Returns:
        Danh sach dict, moi phan tu gom:
            sigma, low_threshold, high_threshold,
            edge_density_percent, processing_time_ms, edges
    """

    threshold_pairs = threshold_pairs or DEFAULT_THRESHOLD_PAIRS
    results = []

    for low_threshold, high_threshold in threshold_pairs:
        start_time = time.perf_counter()

        edges = detect_edges(
            image,
            low_threshold=low_threshold,
            high_threshold=high_threshold,
            sigma=sigma
        )

        elapsed_ms = (time.perf_counter() - start_time) * 1000

        results.append({
            "sigma": sigma,
            "low_threshold": low_threshold,
            "high_threshold": high_threshold,
            "edge_density_percent": round(
                compute_edge_density(edges), 3
            ),
            "processing_time_ms": round(elapsed_ms, 3),
            "edges": edges
        })

    return results


# ---------------------------------------------------------------------------
# Truc quan hoa (Visualization)
# ---------------------------------------------------------------------------

def save_sigma_comparison_figure(results, output_path):
    """
    Ve luoi anh so sanh ket qua Canny ung voi tung gia tri Sigma va
    luu thanh file PNG.

    Parameters:
        results:
            Danh sach ket qua tra ve tu `run_sigma_experiment`.

        output_path:
            Duong dan file PNG can luu.
    """

    figure, axes = plt.subplots(
        1, len(results),
        figsize=(4 * len(results), 4.5)
    )

    if len(results) == 1:
        axes = [axes]

    for axis, result in zip(axes, results):
        axis.imshow(result["edges"], cmap="gray")
        axis.set_title(
            f"sigma = {result['sigma']}\n"
            f"density = {result['edge_density_percent']}%"
        )
        axis.axis("off")

    figure.suptitle(
        "So sanh anh huong cua Sigma den ket qua Canny "
        f"(Low={results[0]['low_threshold']}, "
        f"High={results[0]['high_threshold']})",
        fontsize=13
    )

    figure.tight_layout(rect=[0, 0, 1, 0.90])

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


def save_threshold_comparison_figure(results, output_path):
    """
    Ve luoi anh so sanh ket qua Canny ung voi tung cap Threshold va
    luu thanh file PNG.

    Parameters:
        results:
            Danh sach ket qua tra ve tu `run_threshold_experiment`.

        output_path:
            Duong dan file PNG can luu.
    """

    figure, axes = plt.subplots(
        1, len(results),
        figsize=(4 * len(results), 4.5)
    )

    if len(results) == 1:
        axes = [axes]

    for axis, result in zip(axes, results):
        axis.imshow(result["edges"], cmap="gray")
        axis.set_title(
            f"low={result['low_threshold']}, "
            f"high={result['high_threshold']}\n"
            f"density = {result['edge_density_percent']}%"
        )
        axis.axis("off")

    figure.suptitle(
        "So sanh anh huong cua Threshold den ket qua Canny "
        f"(Sigma={results[0]['sigma']})",
        fontsize=13
    )

    figure.tight_layout(rect=[0, 0, 1, 0.90])

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=150)
    plt.close(figure)


# ---------------------------------------------------------------------------
# Xuat bang ket qua (CSV)
# ---------------------------------------------------------------------------

def save_results_table(sigma_results, threshold_results, output_path):
    """
    Ghi toan bo ket qua cua ca hai thi nghiem ra file CSV.

    Parameters:
        sigma_results:
            Ket qua tra ve tu `run_sigma_experiment`.

        threshold_results:
            Ket qua tra ve tu `run_threshold_experiment`.

        output_path:
            Duong dan file CSV can luu.
    """

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "experiment",
        "sigma",
        "low_threshold",
        "high_threshold",
        "edge_density_percent",
        "processing_time_ms"
    ]

    with open(output_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for result in sigma_results:
            writer.writerow({
                "experiment": "sigma",
                "sigma": result["sigma"],
                "low_threshold": result["low_threshold"],
                "high_threshold": result["high_threshold"],
                "edge_density_percent": result["edge_density_percent"],
                "processing_time_ms": result["processing_time_ms"]
            })

        for result in threshold_results:
            writer.writerow({
                "experiment": "threshold",
                "sigma": result["sigma"],
                "low_threshold": result["low_threshold"],
                "high_threshold": result["high_threshold"],
                "edge_density_percent": result["edge_density_percent"],
                "processing_time_ms": result["processing_time_ms"]
            })


# ---------------------------------------------------------------------------
# Tong hop nhan xet tu ket qua
# ---------------------------------------------------------------------------

def summarize_sigma_trend(results):
    """
    Sinh cau nhan xet ngan gon dua tren xu huong mat do bien khi
    Sigma thay doi (tang dan).

    Parameters:
        results:
            Ket qua tra ve tu `run_sigma_experiment`, phai duoc sap
            xep theo sigma tang dan.

    Returns:
        Chuoi mo ta xu huong.
    """

    first_density = results[0]["edge_density_percent"]
    last_density = results[-1]["edge_density_percent"]

    if last_density < first_density:
        trend = (
            "khi Sigma tang, anh bi lam mo manh hon, cac chi tiet "
            "nho va nhieu bi trieu tieu nen mat do bien phat hien "
            "duoc giam dan"
        )
    else:
        trend = (
            "mat do bien khong giam ro ret khi tang Sigma tren anh "
            "nay, co the do dac diem rieng cua anh dau vao"
        )

    return (
        f"Sigma tu {results[0]['sigma']} den {results[-1]['sigma']}: "
        f"mat do bien tu {first_density}% xuong {last_density}% - {trend}."
    )


def summarize_threshold_trend(results):
    """
    Sinh cau nhan xet ngan gon dua tren xu huong mat do bien khi
    cap Threshold thay doi (tang dan).

    Parameters:
        results:
            Ket qua tra ve tu `run_threshold_experiment`, phai duoc
            sap xep theo threshold tang dan.

    Returns:
        Chuoi mo ta xu huong.
    """

    first_density = results[0]["edge_density_percent"]
    last_density = results[-1]["edge_density_percent"]

    return (
        f"Threshold tu ({results[0]['low_threshold']}, "
        f"{results[0]['high_threshold']}) den "
        f"({results[-1]['low_threshold']}, "
        f"{results[-1]['high_threshold']}): mat do bien tu "
        f"{first_density}% xuong {last_density}% - threshold cang cao, "
        "Canny cang loai bo nhieu canh yeu, chi giu lai cac canh manh."
    )


# ---------------------------------------------------------------------------
# Ham chinh (Entry point)
# ---------------------------------------------------------------------------

def run_experiment(
    input_path=None,
    sigma_values=None,
    threshold_pairs=None
):
    """
    Chay toan bo thi nghiem tham so (Sigma + Threshold) cho TV5:

        1. Nap anh dau vao.
        2. Chay thi nghiem Sigma (EXP-01).
        3. Chay thi nghiem Threshold (EXP-02).
        4. Luu bieu do so sanh (results/figures/).
        5. Luu bang ket qua CSV (results/tables/).
        6. In tom tat nhan xet ra man hinh.

    Parameters:
        input_path:
            Duong dan anh dau vao (tuy chon). Neu None, se tu dong
            tim trong data/input/normal/ hoac tao anh mau.

        sigma_values:
            Danh sach gia tri Sigma can thu nghiem (tuy chon).

        threshold_pairs:
            Danh sach cap (low, high) threshold can thu nghiem (tuy chon).

    Returns:
        Dict chua duong dan cac file ket qua da tao.
    """

    print("=" * 60)
    print("TV5 - PARAMETER EXPERIMENT (Sigma + Threshold)")
    print("=" * 60)

    image, image_name = load_input_image(input_path)
    print(f"[INFO] Anh dau vao: {image_name} - kich thuoc {image.shape}")

    # --- Thi nghiem 1: Sigma ---
    print("\n[1/2] Dang chay thi nghiem Sigma ...")
    sigma_results = run_sigma_experiment(
        image,
        sigma_values=sigma_values
    )

    print(
        f"{'Sigma':>8} | {'Low':>6} | {'High':>6} | "
        f"{'Edge Density (%)':>17} | {'Time (ms)':>10}"
    )
    print("-" * 60)
    for result in sigma_results:
        print(
            f"{result['sigma']:>8} | "
            f"{result['low_threshold']:>6} | "
            f"{result['high_threshold']:>6} | "
            f"{result['edge_density_percent']:>17} | "
            f"{result['processing_time_ms']:>10}"
        )

    # --- Thi nghiem 2: Threshold ---
    print("\n[2/2] Dang chay thi nghiem Threshold ...")
    threshold_results = run_threshold_experiment(
        image,
        threshold_pairs=threshold_pairs
    )

    print(
        f"{'Sigma':>8} | {'Low':>6} | {'High':>6} | "
        f"{'Edge Density (%)':>17} | {'Time (ms)':>10}"
    )
    print("-" * 60)
    for result in threshold_results:
        print(
            f"{result['sigma']:>8} | "
            f"{result['low_threshold']:>6} | "
            f"{result['high_threshold']:>6} | "
            f"{result['edge_density_percent']:>17} | "
            f"{result['processing_time_ms']:>10}"
        )

    # --- Luu bieu do ---
    sigma_figure_path = FIGURES_DIR / "sigma_comparison.png"
    threshold_figure_path = FIGURES_DIR / "threshold_comparison.png"

    save_sigma_comparison_figure(sigma_results, sigma_figure_path)
    save_threshold_comparison_figure(
        threshold_results, threshold_figure_path
    )

    # --- Luu bang CSV ---
    table_path = TABLES_DIR / "parameter_results.csv"
    save_results_table(sigma_results, threshold_results, table_path)

    # --- Nhan xet tong hop ---
    print("\n" + "=" * 60)
    print("NHAN XET TONG HOP")
    print("=" * 60)
    print(summarize_sigma_trend(sigma_results))
    print(summarize_threshold_trend(threshold_results))

    print("\n[OK] Da luu bieu do:")
    print(f"     - {sigma_figure_path}")
    print(f"     - {threshold_figure_path}")
    print(f"[OK] Da luu bang ket qua: {table_path}")

    return {
        "sigma_figure": sigma_figure_path,
        "threshold_figure": threshold_figure_path,
        "table": table_path,
        "sigma_results": sigma_results,
        "threshold_results": threshold_results
    }


if __name__ == "__main__":
    run_experiment()
