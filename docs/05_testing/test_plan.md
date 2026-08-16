# Test Plan

## 1. Mục tiêu

Kiểm tra các chức năng xử lý ảnh và phát hiện cạnh của hệ thống,
đảm bảo chương trình hoạt động đúng với nhiều loại ảnh đầu vào.

## 2. Phạm vi kiểm thử

Các module được kiểm thử:

- Grayscale
- Gaussian Blur
- Canny OpenCV
- Canny Scikit-image
- Sobel
- Laplacian
- Parameter Experiment
- Comparison Experiment

## 3. Dữ liệu kiểm thử

Sử dụng 4 loại ảnh:

- Normal
- Noisy
- Low Contrast
- High Contrast

## 4. Nội dung kiểm thử

Kiểm tra:

- Ảnh có được đọc thành công không.
- Hàm có trả về kết quả không.
- Kích thước output có đúng không.
- Kiểu dữ liệu output có phù hợp không.
- Edge image có được tạo không.
- Kết quả có được lưu thành công không.

## 5. Công cụ

- Python
- OpenCV
- Scikit-image
- Pytest

## 6. Kết quả

Kết quả kiểm thử được ghi nhận trong `test_report.md`.
