# Luồng xử lý ảnh chi tiết (Processing Pipeline)

Phụ trách: TV3 (OpenCV Developer), phối hợp TV1

> Bổ sung chi tiết cho mục 4 của `docs/04_design/system_architecture.md`. Sơ đồ trực quan: xem `docs/04_design/diagrams/processing_pipeline.png` và `docs/04_design/diagrams/system_flow.png`.

## 1. Pipeline chính (đường đi mặc định qua `main.py`)

```
1. load_image(input_path)                      [main.py]
       │
       ▼
2. to_grayscale(image)                          [preprocessing/grayscale.py]
       │
       ▼
3. apply_gaussian_blur(gray, sigma)              [preprocessing/gaussian_blur.py]
       │
       ├──▶ 4a. canny_opencv(blurred, low, high)     [edge_detection/canny_opencv.py]
       ├──▶ 4b. canny_skimage(blurred, sigma)          [edge_detection/canny_skimage.py]
       ├──▶ 4c. sobel_edge(blurred)                    [edge_detection/sobel.py]
       └──▶ 4d. laplacian_edge(blurred)                [edge_detection/laplacian.py]
       │
       ▼
5. save_result(edges, output_path)               [visualization/save_results.py]
```

`--method` trên CLI của `main.py` quyết định nhánh 4a/4b/4c/4d nào được gọi (xem `run_pipeline()` trong `src/main.py`).

## 2. Nhánh thí nghiệm (mở rộng từ pipeline chính)

```
Bộ ảnh mẫu (data/sample/, 4 loại ảnh)
       │
       ▼
Bước 1-3 (grayscale + gaussian blur) — dùng lại nguyên module preprocessing
       │
       ├──▶ parameter_experiment.py    → quét sigma / threshold        (TV5)
       ├──▶ comparison_experiment.py   → so sánh Canny/Sobel/Laplacian (TV6)
       └──▶ image_type_experiment.py   → chạy trên 4 loại ảnh           (TV6)
       │
       ▼
visualization/ (display, plot, save)   → results/figures/, results/tables/
```

Nguyên tắc: các module thí nghiệm **gọi lại** các hàm trong `edge_detection/` và `preprocessing/`, không cài đặt lại thuật toán (đã nêu tại `system_architecture.md`, mục 5).

## 3. Trạng thái dữ liệu qua từng bước

| Bước | Kiểu dữ liệu | Kích thước/định dạng |
|---|---|---|
| Ảnh gốc | numpy array, BGR | (H, W, 3), uint8 |
| Sau grayscale | numpy array | (H, W), uint8 |
| Sau Gaussian blur | numpy array | (H, W), uint8 (hoặc float nếu dùng Scikit-image) |
| Sau edge detection | numpy array nhị phân | (H, W), giá trị {0, 255} hoặc {0, 1} |

## 4. Điểm cần lưu ý khi tích hợp (TV1 tổng hợp)

- Các hàm trong `edge_detection/` phải nhận đúng kiểu dữ liệu ảnh grayscale mà `preprocessing/` trả về — nếu Scikit-image cần ảnh float (0–1) trong khi OpenCV trả ảnh uint8 (0–255), cần có bước convert rõ ràng, tránh để `main.py` tự đoán ngầm.
- `visualization/save_results.py` cần xử lý được cả ảnh nhị phân {0,255} và {0,1} để tương thích cả hai thư viện (xem `canny_algorithm.md`, mục 4 về khác biệt kiểu dữ liệu).
- Khi thêm module mới, cập nhật sơ đồ tại mục 1/2 của tài liệu này và diagram tương ứng trong `diagrams/`.
