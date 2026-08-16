# Timeline — Lab 02: Canny Edge Detection

> Deadline theo ngày trong tuần (1 chu kỳ ~1 tuần, từ thứ 4 đến chủ nhật).
## Bảng deadline 7 thành viên

| Ngày hoàn thành | Thành viên | Phần phụ trách phải hoàn thành |
|---|---|---|
| Thứ 4 | TV1 | Tạo GitHub, cấu trúc project, `README.md`, `requirements.txt`, phân chia branch |
| Thứ 5 | TV2 | Hoàn thành toàn bộ lý thuyết Canny: `canny_theory.md`, `canny_algorithm.md`, `parameter_analysis.md`, `applications.md` |
| Thứ 5 | TV3 | Hoàn thành preprocessing + Canny OpenCV (`grayscale.py`, `gaussian_blur.py`, `canny_opencv.py`) |
| Thứ 5 | TV4 | Hoàn thành Canny Scikit-image + so sánh cơ bản với OpenCV |
| Thứ 6 | TV5 | Hoàn thành toàn bộ thực nghiệm Sigma + Low/High Threshold, lưu kết quả |
| Thứ 6 | TV6 | Hoàn thành Sobel + Laplacian + Canny, thử nghiệm trên các loại ảnh và tạo kết quả so sánh |
| Thứ 7 | TV7 | Hoàn thành Testing + Test Report + tổng hợp kết quả + Conclusion |
| Chủ nhật | Cả nhóm | Tích hợp cuối, sửa lỗi, hoàn thiện báo cáo, README, demo và nộp bài |

## Ghi chú theo từng mốc

- **Thứ 4 (TV1):** là điều kiện tiên quyết — TV2–TV7 chỉ bắt đầu code/viết tài liệu sau khi repo và cấu trúc thư mục đã sẵn sàng.
- **Thứ 5 (TV2, TV3, TV4):** 3 nhánh chạy song song — TV2 làm lý thuyết, TV3/TV4 làm code lõi (preprocessing + 2 cách cài Canny). Đây là điều kiện để TV5, TV6 có module để thực nghiệm.
- **Thứ 6 (TV5, TV6):** thực nghiệm tham số (TV5) và so sánh thuật toán/loại ảnh (TV6) — phải xong trước khi TV7 tổng hợp.
- **Thứ 7 (TV7):** kiểm thử toàn bộ code, viết test report, tổng hợp kết quả từ TV3–TV6 thành `conclusion.md`.
- **Chủ nhật (Cả nhóm):** TV1 tích hợp `main.py` bản đầy đủ, cả nhóm rà soát lỗi, hoàn thiện README và chuẩn bị demo/nộp bài.

## Buổi họp định kỳ

- Họp ngắn mỗi ngày trong tuần deadline: thành viên đến hạn hôm đó báo cáo tiến độ % cho TV1.
- TV1 ghi nhận vào `meeting_notes.md` và cập nhật `task_list.md`.

## Deadline cứng

| Mốc | Ngày | Ghi chú |
|---|---|---|
| TV1 hoàn thành hạ tầng project (Thứ 4) | | Điều kiện để TV2–TV6 bắt đầu |
| Hoàn thành module lõi TV2/TV3/TV4 (Thứ 5) | | Điều kiện để TV5, TV6 bắt đầu thí nghiệm |
| Hoàn thành thí nghiệm TV5/TV6 (Thứ 6) | | Điều kiện để TV7 tổng hợp |
| Hoàn thành test + kết luận TV7 (Thứ 7) | | Điều kiện để TV1 tích hợp cuối |
| Tích hợp cuối + nộp bài (Chủ nhật) | | Deadline chính thức của lớp |
