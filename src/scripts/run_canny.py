import cv2
from pathlib import Path

from src.edge_detection.canny_opencv import detect_edges


# ============================================================
# CẤU HÌNH ĐƯỜNG DẪN
# ============================================================

# Thư mục chứa ảnh đầu vào
INPUT_DIR = Path("data/input")

# Thư mục lưu kết quả Canny OpenCV
OUTPUT_DIR = Path("data/output/opencv")


# ============================================================
# CÁC ĐỊNH DẠNG ẢNH ĐƯỢC HỖ TRỢ
# ============================================================

IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".webp"
}


# ============================================================
# XỬ LÝ MỘT ẢNH
# ============================================================

def process_image(
    image_path,
    output_path,
    low_threshold=100,
    high_threshold=200,
    sigma=1.0
):
    """
    Đọc một ảnh, chạy pipeline Canny OpenCV
    và lưu ảnh kết quả.
    """

    # --------------------------------------------------------
    # 1. Đọc ảnh
    # --------------------------------------------------------

    image = cv2.imread(str(image_path))

    if image is None:
        print(f"[ERROR] Khong doc duoc anh: {image_path}")
        return False


    # --------------------------------------------------------
    # 2. Chạy Canny OpenCV
    #
    # Input
    #   ↓
    # Grayscale
    #   ↓
    # Gaussian Blur
    #   ↓
    # Canny
    #   ↓
    # Output
    # --------------------------------------------------------

    edges = detect_edges(
        image=image,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
        sigma=sigma
    )


    # --------------------------------------------------------
    # 3. Tạo thư mục output
    # --------------------------------------------------------

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    # --------------------------------------------------------
    # 4. Lưu kết quả
    # --------------------------------------------------------

    success = cv2.imwrite(
        str(output_path),
        edges
    )


    if success:
        print(f"[OK] {image_path} -> {output_path}")
        return True

    print(f"[ERROR] Khong luu duoc: {output_path}")
    return False


# ============================================================
# XỬ LÝ TOÀN BỘ ẢNH
# ============================================================

def run_canny():

    print("=" * 60)
    print("CANNY EDGE DETECTOR - OPENCV")
    print("TV3 - OpenCV Developer")
    print("=" * 60)


    # --------------------------------------------------------
    # Thông số Canny
    # --------------------------------------------------------

    low_threshold = 100
    high_threshold = 200
    sigma = 1.0


    print()
    print("Parameters:")
    print(f"  Low threshold  : {low_threshold}")
    print(f"  High threshold : {high_threshold}")
    print(f"  Sigma          : {sigma}")
    print()


    # --------------------------------------------------------
    # Kiểm tra thư mục input
    # --------------------------------------------------------

    if not INPUT_DIR.exists():

        print(
            f"[ERROR] Khong tim thay thu muc: {INPUT_DIR}"
        )

        return


    # --------------------------------------------------------
    # Tìm tất cả ảnh trong data/input
    # --------------------------------------------------------

    image_files = []

    for path in INPUT_DIR.rglob("*"):

        if (
            path.is_file()
            and path.suffix.lower() in IMAGE_EXTENSIONS
        ):
            image_files.append(path)


    image_files.sort()


    print(
        f"Tim thay {len(image_files)} anh."
    )
    print()


    if not image_files:

        print("[ERROR] Khong co anh de xu ly.")
        return


    # --------------------------------------------------------
    # Xử lý từng ảnh
    # --------------------------------------------------------

    success_count = 0
    error_count = 0


    for image_path in image_files:

        # Lấy đường dẫn tương đối so với data/input
        relative_path = image_path.relative_to(
            INPUT_DIR
        )


        # Giữ nguyên cấu trúc thư mục
        # nhưng thêm "_canny" vào tên file

        output_path = (
            OUTPUT_DIR
            / relative_path.parent
            / f"{relative_path.stem}_canny.jpg"
        )


        result = process_image(
            image_path=image_path,
            output_path=output_path,
            low_threshold=low_threshold,
            high_threshold=high_threshold,
            sigma=sigma
        )


        if result:
            success_count += 1
        else:
            error_count += 1


    # ========================================================
    # TỔNG KẾT
    # ========================================================

    print()
    print("=" * 60)
    print("KET QUA")
    print("=" * 60)

    print(f"Tong so anh : {len(image_files)}")
    print(f"Thanh cong  : {success_count}")
    print(f"Loi         : {error_count}")

    print()
    print(f"Output: {OUTPUT_DIR}")

    print("=" * 60)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    run_canny()
