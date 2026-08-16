# Kiến trúc hệ thống — Lab 02: Canny Edge Detection

## 1. Tổng quan

Hệ thống được tổ chức theo kiến trúc **module hóa theo pipeline**: mỗi bước xử lý ảnh là một module độc lập, có thể test riêng, và được `main.py` ghép lại thành pipeline hoàn chỉnh.

```
┌─────────────┐   ┌────────────────┐   ┌──────────────────┐   ┌─────────────── ┐
│   data/     │──▶│ preprocessing/ │──▶│  edge_detection/ | ──▶│ visualization/│
│  (input)    │   │ grayscale,     │   │ canny_opencv,    |   │ display,       │
│             │   │ gaussian_blur  │   │ canny_skimage,   │   │ plot, save     │
│             │   │                │   │ sobel, laplacian │   │                │
└─────────────┘   └────────────────┘   └──────────────────┘   └─────────────── ┘
                                                │
                                                ▼
                                       ┌──────────────────┐
                                       │   experiments/   |
                                       │ parameter, image_│
                                       │ type, comparison │
                                       └──────────────────┘
                                                │
                                                ▼
                                       ┌──────────────────┐
                                       │    results/      │
                                       │ figures, tables, │
                                       │ reports          │
                                       └──────────────────┘
```

`src/main.py` đóng vai trò **orchestrator**: nhận ảnh đầu vào, gọi lần lượt các module preprocessing → edge_detection → (tuỳ chọn) experiments → visualization, và ghi kết quả ra `results/` hoặc `data/output/`.

## 2. Các module & trách nhiệm

| Module | Thư mục | Phụ trách | Vai trò |
|---|---|---|---|
| Preprocessing | `src/preprocessing/` | TV3 | Chuyển ảnh sang grayscale, làm mờ Gaussian |
| Edge Detection | `src/edge_detection/` | TV3, TV4, TV6 | Canny (OpenCV/Scikit-image), Sobel, Laplacian |
| Experiments | `src/experiments/` | TV5, TV6 | Thí nghiệm tham số, so sánh loại ảnh, so sánh thuật toán |
| Visualization | `src/visualization/` | TV3, TV5, TV6, TV1 | Hiển thị, vẽ biểu đồ, lưu kết quả |
| Main / Integration | `src/main.py` | TV1 | Ghép toàn bộ pipeline, giao diện dòng lệnh (CLI) |

## 3. Nguyên tắc thiết kế

1. **Tách biệt trách nhiệm (Separation of Concerns):** mỗi module chỉ làm một việc (ví dụ `canny_opencv.py` không tự đọc ảnh từ đĩa, việc đó do `main.py` hoặc một hàm I/O chung đảm nhận).
2. **Interface thống nhất:** các hàm phát hiện biên (Canny OpenCV, Canny Scikit-image, Sobel, Laplacian) nên nhận vào một ảnh grayscale (numpy array) và trả về một ảnh nhị phân biên (numpy array), để `main.py` và `comparison_experiment.py` có thể gọi thay thế cho nhau dễ dàng.
3. **Không hard-code đường dẫn:** đường dẫn ảnh input/output truyền qua tham số CLI hoặc file cấu hình, không viết cứng trong code.
4. **Test độc lập từng module:** mỗi module trong `src/` có test tương ứng trong `tests/`, TV1 chỉ tích hợp sau khi module đã có test pass.

## 4. Luồng xử lý ảnh (tóm tắt)

```
Input image
     ↓ (TV3)
Grayscale
     ↓ (TV3)
Gaussian Blur
     ↓
     ├──▶ Canny OpenCV      
     ├──▶ Canny Scikit-image 
     ├──▶ Sobel             
     └──▶ Laplacian          
     ↓
Visualization / So sánh / Lưu kết quả
```

Chi tiết luồng xử lý đầy đủ (bao gồm các nhánh thí nghiệm): xem `docs/04_design/processing_pipeline.md` (TV3 phụ trách).

## 5. Quyết định kiến trúc quan trọng

| Quyết định | Lý do |
|---|---|
| Tách `preprocessing` và `edge_detection` thành 2 package riêng | Cho phép tái sử dụng bước tiền xử lý cho cả Canny, Sobel, Laplacian mà không lặp code |
| `experiments/` gọi vào `edge_detection/` thay vì cài lại thuật toán | Tránh trùng lặp logic, đảm bảo kết quả thí nghiệm nhất quán với module chính |
| `main.py` chỉ orchestrate, không chứa logic xử lý ảnh | Giữ `main.py` ngắn gọn, dễ tích hợp module mới về sau |

Các quyết định phát sinh trong quá trình làm việc được ghi tiếp vào `docs/07_history/decision_log.md`.
