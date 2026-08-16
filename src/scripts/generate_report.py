from pathlib import Path
import subprocess
from datetime import datetime


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

# Project root
# generate_report.py nằm trong:
# scripts/generate_report.py
#
# Vì vậy parents[1] sẽ trỏ về thư mục project.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Folder lưu report
REPORT_DIR = PROJECT_ROOT / "results" / "reports"

# File report
REPORT_FILE = REPORT_DIR / "test_summary.md"


# ============================================================
# RUN TESTS
# ============================================================

def run_tests():
    """
    Run all project tests using pytest.
    """

    result = subprocess.run(
        ["python", "-m", "pytest", "-v"],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True
    )

    return result


# ============================================================
# GENERATE REPORT
# ============================================================

def generate_report(test_result):
    """
    Generate a Markdown test summary report.
    """

    # Create report folder if it does not exist
    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Pytest return code:
    # 0 = all tests passed
    # other values = failed/error
    passed = test_result.returncode == 0

    status = "PASS" if passed else "FAIL"

    # --------------------------------------------------------
    # Basic information
    # --------------------------------------------------------

    # Tách riêng để tránh dùng dấu " lồng trong f-string """
    # (lỗi cú pháp trên Python < 3.12)
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""# Test Summary Report

## 1. Thông tin

- Thời gian: {now_str}
- Công cụ: Pytest
- Trạng thái: **{status}**

## 2. Kết quả kiểm thử

```text
{test_result.stdout}
```

"""

    # --------------------------------------------------------
    # Error information
    # --------------------------------------------------------

    if test_result.stderr:
        report += f"""## 3. Lỗi

```text
{test_result.stderr}
```

"""
    else:
        report += """## 3. Lỗi

Không có lỗi được ghi nhận.

"""

    # --------------------------------------------------------
    # Evaluation
    # --------------------------------------------------------

    report += """## 4. Đánh giá

Các test được chạy tự động bằng Pytest.

Các module chính được kiểm thử:

Grayscale
Gaussian Blur
Canny OpenCV
Canny Scikit-image
Parameter Experiment
Sobel
Laplacian
Image Type Experiment
Comparison
Pipeline

Nếu tất cả test đều PASSED, hệ thống được đánh giá là đạt yêu cầu kiểm thử.

Nếu có test FAILED hoặc ERROR, cần kiểm tra và sửa lỗi trước khi đánh giá phiên bản cuối cùng.

## 5. Kết luận

Kết quả kiểm thử được sử dụng để đánh giá tính đúng đắn và khả năng hoạt động của các module xử lý ảnh và phát hiện cạnh.

Report này được tạo tự động bằng script generate_report.py.
"""

    # --------------------------------------------------------
    # Save report
    # --------------------------------------------------------

    REPORT_FILE.write_text(
        report,
        encoding="utf-8"
    )

    print("=" * 60)
    print("TEST REPORT GENERATED")
    print("=" * 60)
    print(f"Status : {status}")
    print(f"File   : {REPORT_FILE}")

def main():
    print("=" * 60)
    print("RUNNING PROJECT TESTS")
    print("=" * 60)

    test_result = run_tests()

    generate_report(test_result)

if __name__ == "__main__":
    main()
