# AI Usage Log

## 1. Mục đích sử dụng AI

AI được sử dụng để hỗ trợ trong quá trình phát triển, kiểm thử và hoàn thiện bài thực hành xử lý ảnh.

AI không thay thế việc chạy chương trình và kiểm thử thực tế. Các kết quả cuối cùng được kiểm tra lại bằng Pytest trên môi trường thực tế của project.

---

## 2. Các nội dung đã sử dụng AI hỗ trợ

### 2.1. Hỗ trợ giải thích code

AI được sử dụng để:

- Giải thích cách hoạt động của Grayscale.
- Giải thích Gaussian Blur.
- Giải thích Canny Edge Detection.
- Giải thích Sobel và Laplacian.
- Giải thích các tham số như Sigma, Low Threshold và High Threshold.
- Giải thích cách sử dụng Pytest.

### 2.2. Hỗ trợ viết và sửa test

AI được sử dụng để hỗ trợ xây dựng các test case cho:

- Grayscale
- Gaussian Blur
- Canny OpenCV
- Canny Scikit-image
- Parameter Experiment
- Sobel
- Laplacian
- Image Type Experiment
- Comparison
- Pipeline

Các test sau đó được chạy thực tế bằng Pytest để kiểm tra kết quả.

### 2.3. Hỗ trợ sửa lỗi

AI được sử dụng để phân tích một số lỗi trong quá trình chạy test, ví dụ:

- Import module không đúng.
- Sai đường dẫn project.
- Lỗi khi chạy `pytest`.
- Lỗi liên quan đến cấu trúc thư mục.
- Lỗi khi tạo test report.

Sau khi nhận hướng dẫn, code được chỉnh sửa và chạy lại để xác nhận.

### 2.4. Hỗ trợ tạo báo cáo

AI được sử dụng để hỗ trợ tạo:

- `test_summary.md`
- `conclusion.md`
- `generate_report.py`
- `ai_usage_log.md`

Các file được kiểm tra lại và điều chỉnh theo cấu trúc của project.

---

## 3. Các module được kiểm thử

Các module chính đã được kiểm thử bằng Pytest gồm:

- Grayscale
- Gaussian Blur
- Canny OpenCV
- Canny Scikit-image
- Parameter Experiment
- Sobel
- Laplacian
- Image Type Experiment
- Comparison
- Pipeline

---

## 4. Kết quả kiểm thử

Các test đã được chạy bằng lệnh:

```bash
python -m pytest -v
