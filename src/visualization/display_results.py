import cv2
import matplotlib.pyplot as plt
from pathlib import Path


# ============================================================
# HIỂN THỊ ẢNH INPUT VÀ KẾT QUẢ CANNY
# ============================================================

def display_results(
    input_path,
    output_path,
    title="Canny OpenCV Result"
):
    """
    Hiển thị ảnh đầu vào và ảnh kết quả Canny cạnh nhau.

    Parameters:
        input_path:
            Đường dẫn đến ảnh đầu vào.

        output_path:
            Đường dẫn đến ảnh kết quả Canny.

        title:
            Tiêu đề của hình hiển thị.
    """

    # --------------------------------------------------------
    # 1. Đọc ảnh đầu vào
    # --------------------------------------------------------

    input_image = cv2.imread(
        str(input_path)
    )

    if input_image is None:
        raise FileNotFoundError(
            f"Khong the doc anh input: {input_path}"
        )


    # --------------------------------------------------------
    # 2. Đọc ảnh kết quả Canny
    # --------------------------------------------------------

    output_image = cv2.imread(
        str(output_path),
        cv2.IMREAD_GRAYSCALE
    )

    if output_image is None:
        raise FileNotFoundError(
            f"Khong the doc anh output: {output_path}"
        )


    # --------------------------------------------------------
    # 3. Chuyển ảnh BGR → RGB
    #
    # OpenCV đọc ảnh theo BGR.
    # Matplotlib hiển thị theo RGB.
    # --------------------------------------------------------

    input_rgb = cv2.cvtColor(
        input_image,
        cv2.COLOR_BGR2RGB
    )


    # --------------------------------------------------------
    # 4. Tạo cửa sổ hiển thị
    # --------------------------------------------------------

    plt.figure(
        figsize=(12, 5)
    )


    # --------------------------------------------------------
    # 5. Hiển thị ảnh input
    # --------------------------------------------------------

    plt.subplot(
        1,
        2,
        1
    )

    plt.imshow(
        input_rgb
    )

    plt.title(
        "Input Image"
    )

    plt.axis(
        "off"
    )


    # --------------------------------------------------------
    # 6. Hiển thị ảnh Canny
    # --------------------------------------------------------

    plt.subplot(
        1,
        2,
        2
    )

    plt.imshow(
        output_image,
        cmap="gray"
    )

    plt.title(
        "Canny OpenCV"
    )

    plt.axis(
        "off"
    )


    # --------------------------------------------------------
    # 7. Tiêu đề chung
    # --------------------------------------------------------

    plt.suptitle(
        title
    )

    plt.tight_layout()


    # --------------------------------------------------------
    # 8. Hiển thị
    # --------------------------------------------------------

    plt.show()


# ============================================================
# HIỂN THỊ ẢNH THEO TÊN FILE
# ============================================================

def display_single_result(
    input_path,
    output_path
):
    """
    Hàm tiện ích để hiển thị một kết quả Canny.
    """

    input_path = Path(input_path)
    output_path = Path(output_path)

    display_results(
        input_path=input_path,
        output_path=output_path,
        title=f"Canny Result - {input_path.name}"
    )


# ============================================================
# CHẠY THỬ
# ============================================================

if __name__ == "__main__":

    # --------------------------------------------------------
    # Ví dụ:
    #
    # data/input/normal/normal_01.jpg
    #
    # →
    #
    # data/output/opencv/normal/normal_01_canny.jpg
    # --------------------------------------------------------

    input_path = Path(
        "data/input/normal/normal_01.jpg"
    )

    output_path = Path(
        "data/output/opencv/normal/normal_01_canny.jpg"
    )


    display_single_result(
        input_path=input_path,
        output_path=output_path
    )
