# Test Report

## 1. Tổng quan

Mục tiêu của kiểm thử là xác nhận các module xử lý ảnh và phát hiện cạnh
hoạt động đúng theo yêu cầu.

Công cụ kiểm thử:

- Python
- Pytest
- OpenCV
- Scikit-image

## 2. Kết quả kiểm thử

| Test Case | Module | Kết quả | Trạng thái |
|---|---|---:|---|
| TC01 | Grayscale | 4/4 passed | PASS |
| TC02 | Gaussian Blur | 4/4 passed | PASS |
| TC03 | Canny OpenCV | 4/4 passed | PASS |
| TC04 | Canny Scikit-image | 4/4 passed | PASS |
| TC05 | Sobel | 4/4 passed | PASS |
| TC06 | Laplacian | 4/4 passed | PASS |
| TC07 | Parameter - Sigma | 1/1 passed | PASS |
| TC08 | Parameter - Threshold | 1/1 passed | PASS |
| TC09 | Comparison | 4/4 passed | PASS |
| TC10 | Image Type | 1/1 passed | PASS |

## 3. Chi tiết kiểm thử

### TC01 - Grayscale

Kiểm tra chuyển đổi ảnh sang ảnh grayscale với 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Output được tạo thành công.
- Kích thước output phù hợp.
- Module hoạt động đúng.

### TC02 - Gaussian Blur

Kiểm tra Gaussian Blur trên 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Output được tạo thành công.
- Kích thước output giống ảnh đầu vào.

### TC03 - Canny OpenCV

Kiểm tra phát hiện cạnh bằng OpenCV Canny trên 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Edge image được tạo thành công.
- Output có kích thước phù hợp.

### TC04 - Canny Scikit-image

Kiểm tra phát hiện cạnh bằng Scikit-image trên 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Edge image được tạo thành công.
- Output hợp lệ.

### TC05 - Sobel

Kiểm tra phát hiện cạnh bằng Sobel trên 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Edge image được tạo thành công.
- Kích thước output phù hợp.

### TC06 - Laplacian

Kiểm tra phát hiện cạnh bằng Laplacian trên 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Edge image được tạo thành công.
- Kích thước output phù hợp.

### TC07 - Parameter Experiment: Sigma

Kiểm tra thử nghiệm với nhiều giá trị Sigma khác nhau.

Các giá trị được kiểm tra gồm:

- Sigma = 0.5
- Sigma = 1.0

**Kết quả:** Test Sigma experiment passed.

- Kết quả được tạo cho tất cả giá trị Sigma.
- Edge image được tạo thành công.
- Edge density được tính toán.

### TC08 - Parameter Experiment: Threshold

Kiểm tra thử nghiệm với các cặp Low Threshold và High Threshold.

Ví dụ:

- (50, 100)
- (50, 150)
- (100, 200)

**Kết quả:** Test Threshold experiment passed.

- Kết quả được tạo cho các cặp threshold.
- Edge image được tạo thành công.
- Các thông số được ghi nhận.

### TC09 - Comparison

Kiểm tra so sánh Canny, Sobel và Laplacian trên 4 loại ảnh.

**Kết quả:** 4/4 test passed.

- Ảnh đầu vào được đọc thành công.
- Kết quả so sánh được tạo.
- Kích thước ảnh so sánh đúng.
- Ảnh kết quả được lưu thành công.

### TC10 - Image Type

Kiểm tra tạo ảnh Noisy, Low Contrast và High Contrast từ ảnh Normal.

**Kết quả:** Test passed.

- Ba ảnh được tạo thành công.
- Kích thước ảnh không thay đổi.
- Kiểu dữ liệu output phù hợp.
- Các ảnh được lưu thành công.

## 4. Tổng kết

Tất cả các test case đã thực hiện đều **PASS**.

Các module chính của hệ thống gồm:

- Grayscale
- Gaussian Blur
- Canny OpenCV
- Canny Scikit-image
- Sobel
- Laplacian
- Parameter Experiment
- Comparison Experiment
- Image Type Experiment

đều hoạt động đúng theo các tiêu chí kiểm thử đã đặt ra.

## 5. Kết luận

Kết quả kiểm thử cho thấy hệ thống xử lý ảnh và phát hiện cạnh hoạt động
ổn định với các loại ảnh được sử dụng trong project.

Không phát hiện lỗi trong các test case đã thực hiện.
