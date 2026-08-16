# Experiment Log - TV3 OpenCV

## 1. Thông tin

- Thành viên: TV3
- Module: OpenCV Canny Edge Detector
- Thư viện: OpenCV
- Hàm chính: `cv2.Canny()`

---

## 2. Pipeline

Input Image
→ Grayscale
→ Gaussian Blur
→ Canny
→ Output Edge Image

---

# 3. Experiment 1 - Ảnh bình thường

## Input

Sử dụng 5 ảnh:

- normal_01.jpg
- normal_02.jpg
- normal_03.jpg
- normal_04.jpg
- normal_05.jpg

## Parameters

- Gaussian Kernel: (5, 5)
- Sigma: 1.0
- Low Threshold: 100
- High Threshold: 200

## Nhận xét

Canny phát hiện được các đường biên chính
của các đối tượng trong ảnh.

---

# 4. Experiment 2 - Ảnh nhiễu

## Input

Sử dụng các ảnh trong:

`data/input/noisy/`

## Parameters

- Gaussian Kernel: (5, 5)
- Sigma: 1.0
- Low Threshold: 100
- High Threshold: 200

## Nhận xét

Ảnh nhiễu có thể tạo ra nhiều cạnh không mong muốn.

Gaussian Blur giúp giảm ảnh hưởng của nhiễu
trước khi thực hiện thuật toán Canny.

---

# 5. Experiment 3 - Thay đổi Threshold

| STT | Low | High |
|---|---:|---:|
| 1 | 50 | 100 |
| 2 | 50 | 150 |
| 3 | 100 | 200 |
| 4 | 100 | 250 |
| 5 | 150 | 300 |

## Nhận xét

Khi threshold thấp, Canny có xu hướng phát hiện
nhiều cạnh hơn.

Khi threshold cao, các cạnh yếu có thể bị loại bỏ.

Giá trị 100/200 được sử dụng làm cấu hình mặc định
cho các thí nghiệm ban đầu.

---

# 6. Kết luận

Thí nghiệm cho thấy kết quả Canny phụ thuộc đáng kể
vào các tham số threshold và sigma.

Gaussian Blur giúp giảm nhiễu trước khi phát hiện cạnh.

Việc lựa chọn threshold phù hợp giúp cân bằng giữa
việc phát hiện đủ cạnh và hạn chế các cạnh giả.