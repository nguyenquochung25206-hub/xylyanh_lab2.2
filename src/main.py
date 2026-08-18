import argparse
from pathlib import Path

import cv2

from src.edge_detection.canny_opencv import detect_edges as canny_opencv
from src.edge_detection.canny_skimage import canny_skimage
from src.edge_detection.sobel import detect_edges as sobel
from src.edge_detection.laplacian import detect_edges as laplacian


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp",
}


def get_input_images(input_path):
    """
    Nhận file ảnh hoặc thư mục chứa ảnh.

    Nếu là file:
        trả về [file]

    Nếu là thư mục:
        tìm tất cả ảnh bên trong.
    """

    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(
            f"Không tồn tại đường dẫn: {path}"
        )

    # Nếu input là một file ảnh
    if path.is_file():

        if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"File không phải ảnh: {path}"
            )

        return [path]

    # Nếu input là thư mục
    if path.is_dir():

        images = sorted(
            file
            for file in path.iterdir()
            if file.is_file()
            and file.suffix.lower() in SUPPORTED_EXTENSIONS
        )

        if not images:
            raise FileNotFoundError(
                f"Không tìm thấy ảnh trong: {path}"
            )

        return images

    raise ValueError(
        f"Input không hợp lệ: {path}"
    )


def run_method(
    image,
    method,
    sigma,
    low,
    high
):
    """
    Chọn thuật toán xử lý ảnh.
    """

    if method == "opencv":

        return canny_opencv(
            image,
            low_threshold=low,
            high_threshold=high,
            sigma=sigma
        )

    elif method == "skimage":

        return canny_skimage(
            image,
            sigma=sigma,
            low_threshold=low,
            high_threshold=high
        )

    elif method == "sobel":

        return sobel(
            image,
            kernel_size=3,
            sigma=sigma
        )

    elif method == "laplacian":

        return laplacian(
            image,
            kernel_size=3,
            sigma=sigma
        )

    else:

        raise ValueError(
            f"Method không hợp lệ: {method}"
        )


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Image Edge Detection - "
            "Canny OpenCV / Canny Scikit-image / "
            "Sobel / Laplacian"
        )
    )

    parser.add_argument(
        "--input",
        required=True,
        help=(
            "Đường dẫn đến một ảnh "
            "hoặc thư mục chứa ảnh"
        )
    )

    parser.add_argument(
        "--output",
        default="results",
        help="Thư mục lưu kết quả"
    )

    parser.add_argument(
        "--method",
        choices=[
            "opencv",
            "skimage",
            "sobel",
            "laplacian"
        ],
        default="opencv",
        help="Thuật toán phát hiện cạnh"
    )

    parser.add_argument(
        "--sigma",
        type=float,
        default=1.0,
        help="Sigma của Gaussian Blur"
    )

    parser.add_argument(
        "--low",
        type=float,
        default=50,
        help="Low threshold của Canny"
    )

    parser.add_argument(
        "--high",
        type=float,
        default=150,
        help="High threshold của Canny"
    )

    args = parser.parse_args()

    # --------------------------------
    # Lấy danh sách ảnh
    # --------------------------------

    images = get_input_images(
        args.input
    )

    print()
    print("=" * 60)
    print("IMAGE EDGE DETECTION")
    print("=" * 60)
    print(f"Input       : {args.input}")
    print(f"Method      : {args.method}")
    print(f"Sigma       : {args.sigma}")
    print(f"Low         : {args.low}")
    print(f"High        : {args.high}")
    print(f"Số lượng ảnh: {len(images)}")
    print("=" * 60)
    print()

    # --------------------------------
    # Tạo thư mục output
    # --------------------------------

    output_dir = (
        Path(args.output)
        / args.method
    )

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    # --------------------------------
    # Xử lý từng ảnh
    # --------------------------------

    for index, image_path in enumerate(
        images,
        start=1
    ):

        print(
            f"[{index}/{len(images)}] "
            f"Đang xử lý: {image_path.name}"
        )

        # Đọc ảnh
        image = cv2.imread(
            str(image_path)
        )

        if image is None:

            print(
                f"  [SKIP] Không đọc được: "
                f"{image_path}"
            )

            continue

        try:

            # Chạy thuật toán
            result = run_method(
                image=image,
                method=args.method,
                sigma=args.sigma,
                low=args.low,
                high=args.high
            )

            # Tên file output
            output_file = (
                output_dir
                / f"{image_path.stem}_{args.method}.png"
            )

            # Lưu ảnh
            cv2.imwrite(
                str(output_file),
                result
            )

            print(
                f"  [OK] → {output_file}"
            )

        except Exception as e:

            print(
                f"  [ERROR] {image_path.name}: "
                f"{e}"
            )

    print()
    print("=" * 60)
    print("HOÀN TẤT!")
    print(
        f"Kết quả nằm trong: {output_dir}"
    )
    print("=" * 60)


if __name__ == "__main__":
    main()