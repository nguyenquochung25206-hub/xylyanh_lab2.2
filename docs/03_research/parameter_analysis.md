Parameter Analysis — Ảnh hưởng của tham số đến Canny Edge Detection
Phụ trách: TV2 (cơ sở lý thuyết) + TV5 (thực nghiệm và số liệu)
Phần dưới đây do TV5 biên soạn, dựa trên kết quả chạy thực tế của
`src/experiments/parameter_experiment.py`.
---
1. Các tham số được khảo sát
Canny Edge Detection (qua `cv2.Canny`) trong project sử dụng 3 tham số
chính có thể điều chỉnh:
Tham số	Vai trò	File cấu hình
`sigma`	Độ lệch chuẩn của Gaussian Blur, kiểm soát mức độ làm mờ/khử nhiễu trước khi tính gradient.	`src/preprocessing/gaussian_blur.py`
`low_threshold`	Ngưỡng dưới của Double Threshold — biên có gradient thấp hơn ngưỡng này bị loại bỏ.	`src/edge_detection/canny_opencv.py`
`high_threshold`	Ngưỡng trên của Double Threshold — biên có gradient cao hơn ngưỡng này được coi là biên mạnh (chắc chắn giữ lại).	`src/edge_detection/canny_opencv.py`
---
2. Cơ sở lý thuyết ngắn gọn
2.1. Sigma (Gaussian Blur)
Gaussian Blur được áp dụng trước Canny để giảm nhiễu, vì thuật toán Canny
tính đạo hàm (gradient) của ảnh — nhiễu sẽ tạo ra rất nhiều gradient giả,
dẫn đến phát hiện sai cạnh. Sigma càng lớn, kernel Gaussian càng "trải
rộng", ảnh bị làm mờ càng nhiều:
Sigma nhỏ → giữ được nhiều chi tiết, nhưng cũng giữ lại nhiều nhiễu.
Sigma lớn → khử nhiễu tốt hơn, nhưng có thể làm mất các cạnh nhỏ, mảnh,
hoặc làm hai cạnh gần nhau bị "dính" lại thành một.
2.2. Double Threshold (Low / High)
Sau bước Non-Maximum Suppression, mỗi pixel biên tiềm năng được phân loại
dựa trên độ lớn gradient so với hai ngưỡng:
Gradient > `high_threshold` → biên mạnh (strong edge), luôn được giữ.
`low_threshold` < Gradient ≤ `high_threshold` → biên yếu (weak edge),
chỉ được giữ nếu liên kết (connected) với một biên mạnh (Edge
Tracking by Hysteresis).
Gradient ≤ `low_threshold` → bị loại bỏ hoàn toàn.
Vì vậy threshold càng cao thì tiêu chuẩn để một pixel được công nhận là
biên càng khắt khe, kết quả thu được càng "sạch" nhưng có thể bỏ sót các
cạnh yếu, mờ trong ảnh.
---
3. Thiết kế thực nghiệm
Thực nghiệm được thực hiện bởi `src/experiments/parameter_experiment.py`,
theo 2 nhóm độc lập để cô lập ảnh hưởng của từng tham số:
```text
Thí nghiệm 1 (EXP-01): Cố định Low=100, High=200
    Sigma = 0.5 → 1.0 → 1.5 → 2.0 → 3.0

Thí nghiệm 2 (EXP-02): Cố định Sigma=1.0
    (Low, High) = (50,100) → (50,150) → (100,200) → (100,250) → (150,300)
```
Chỉ số định lượng dùng để so sánh: mật độ biên (edge density) — tỷ lệ
phần trăm số pixel được xác định là biên trên tổng số pixel của ảnh — và
thời gian xử lý (ms).
---
4. Kết quả và nhận xét
Kết quả số liệu chi tiết được lưu tại `results/tables/parameter_results.csv`
và biểu đồ trực quan tại `results/figures/`. Nhận xét đầy đủ, bao gồm câu
trả lời cho các câu hỏi bắt buộc của đề bài, được trình bày tại
`docs/06_results/parameter_comparison.md`.
Tóm tắt xu hướng quan sát được:
Sigma tăng → ảnh bị làm mờ nhiều hơn → mật độ biên phát hiện được
có xu hướng giảm dần, các cạnh trở nên mượt hơn nhưng có thể mất
chi tiết nhỏ.
Threshold tăng (cả Low lẫn High) → tiêu chuẩn nhận biên khắt khe
hơn → mật độ biên giảm, chỉ còn lại các cạnh có gradient mạnh.
---
5. Tài liệu liên quan
`docs/03_research/canny_theory.md` — Lý thuyết chi tiết từng bước của
Canny (TV2).
`docs/06_results/parameter_comparison.md` — Bảng kết quả đầy đủ và trả
lời câu hỏi của đề (TV5).
`docs/07_history/experiment_log.md` — Nhật ký thí nghiệm.
