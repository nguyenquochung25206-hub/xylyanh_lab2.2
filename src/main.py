import argparse
import os
import cv2

from src.edge_detection.canny_opencv import detect_edges as canny_opencv
from src.edge_detection.canny_skimage import canny_skimage
from src.edge_detection.sobel import detect_edges as sobel_edge
from src.edge_detection.laplacian import detect_edges as laplacian_edge
from src.visualization.save_results import save_result

METHODS = {
    "opencv": canny_opencv,
    "skimage": canny_skimage,
    "sobel": sobel_edge,
    "laplacian": laplacian_edge,
}


def load_image(path):
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"Không đọc được ảnh: {path}")
    return image


def run_pipeline(input_path, output_path, method, sigma, low, high):
    image = load_image(input_path)

    # Edge detection — truyền ảnh gốc (BGR), mỗi hàm tự lo tiền xử lý bên trong
    if method == "opencv":
        edges = canny_opencv(image, low_threshold=low, high_threshold=high, sigma=sigma)
    elif method == "skimage":
        # canny_skimage dùng color.rgb2gray() bên trong, vốn kỳ vọng thứ tự
        # kênh RGB — trong khi cv2.imread() trả về BGR. Cần đổi thứ tự kênh
        # trước khi truyền vào, nếu không trọng số grayscale sẽ bị sai
        # (đổi chỗ kênh đỏ/xanh dương), khiến kết quả so sánh OpenCV vs
        # Scikit-image không công bằng.
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        edges = canny_skimage(image_rgb, sigma=sigma)
    else:
        edges = METHODS[method](image, sigma=sigma)

    save_result(edges, output_path)
    print(f"[OK] Đã lưu: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Canny Edge Detection Pipeline")
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default=None)
    parser.add_argument(
        "--method",
        choices=METHODS.keys(),
        default="opencv")
    parser.add_argument("--sigma", type=float, default=1.0)
    parser.add_argument("--low", type=int, default=100)
    parser.add_argument("--high", type=int, default=200)
    args = parser.parse_args()
    if args.output is None:
        name = os.path.splitext(os.path.basename(args.input))[0]
        args.output = f"data/output/{args.method}/{name}_{args.method}.png"
    run_pipeline(
        args.input,
        args.output,
        args.method,
        args.sigma,
        args.low,
        args.high)


if __name__ == "__main__":
    main()
