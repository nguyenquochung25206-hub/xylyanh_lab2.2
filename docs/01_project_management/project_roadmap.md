# Roadmap Project — Lab 02: Canny Edge Detection

## Giai đoạn 1 — Khởi tạo & Nghiên cứu
**Phụ trách chính:** TV1 (hạ tầng), TV2 (lý thuyết)

- TV1: tạo repository, cấu trúc thư mục, README, requirements.
- TV2: nghiên cứu lý thuyết Canny (`canny_theory.md`, `canny_algorithm.md`).
- TV1: soạn `lab_requirements.md` cùng TV2 để chuyển đề bài thành các REQ cụ thể.

**Đầu ra:** Cấu trúc project sẵn sàng, tài liệu lý thuyết nháp đầu tiên.

## Giai đoạn 2 — Phát triển module lõi
**Phụ trách chính:** TV3, TV4

- TV3: `grayscale.py`, `gaussian_blur.py`, `canny_opencv.py`.
- TV4: `canny_skimage.py`, phân tích khác biệt OpenCV vs Scikit-image.
- TV1: theo dõi tiến độ, review code, chuẩn bị `system_architecture.md`.

**Đầu ra:** Pipeline Canny chạy được bằng cả hai thư viện trên ảnh mẫu.

## Giai đoạn 3 — Thực nghiệm
**Phụ trách chính:** TV5, TV6

- TV5: thí nghiệm Sigma và Threshold (`parameter_experiment.py`).
- TV6: so sánh Sobel/Laplacian/Canny và chạy trên 4 loại ảnh.
- TV1: hỗ trợ tích hợp kết quả thí nghiệm vào pipeline chung, cập nhật `processing_pipeline.md` cùng TV3.

**Đầu ra:** Bảng/biểu đồ kết quả thí nghiệm (`results/figures/`, `results/tables/`).

## Giai đoạn 4 — Kiểm thử & Tổng hợp
**Phụ trách chính:** TV7

- TV7: viết test cho các module (`tests/`), viết `test_report.md`.
- TV7: tổng hợp kết quả từ TV3–TV6 vào `experiment_results.md`, `conclusion.md`.
- TV1: kiểm tra toàn bộ pipeline end-to-end, hoàn thiện `main.py`.

**Đầu ra:** Báo cáo kết quả hoàn chỉnh, toàn bộ test pass.

## Giai đoạn 5 — Tích hợp cuối & Bàn giao
**Phụ trách chính:** TV1

- TV1: tích hợp toàn bộ module vào `main.py`, chạy lại pipeline tổng.
- TV1: hoàn thiện README, CHANGELOG, đóng gói báo cáo cuối cùng (`results/reports/`).
- Cả nhóm: rà soát lần cuối, mỗi người xác nhận phần của mình.

**Đầu ra:** Project hoàn chỉnh, sẵn sàng nộp/bảo vệ.

