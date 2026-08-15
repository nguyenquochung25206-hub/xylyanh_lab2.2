Experiment Requirements
Phụ trách: TV5 — Parameter Experiment
Liên quan: `docs/02_requirements/lab_requirements.md` (TV2)
---
1. Mục đích
Tài liệu này chuyển yêu cầu "thay đổi tham số và quan sát kết quả" của đề bài
thành các yêu cầu thực nghiệm cụ thể (Experiment Requirements — EXP), làm cơ
sở để triển khai code (`src/experiments/parameter_experiment.py`) và tổng
hợp kết quả (`docs/06_results/parameter_comparison.md`).
---
2. Danh sách yêu cầu thực nghiệm
Mã	Nội dung	Input	Output mong đợi
EXP-01	Thay đổi giá trị Sigma của Gaussian Blur, giữ nguyên Low/High Threshold, quan sát ảnh hưởng đến kết quả Canny.	Sigma = 0.5, 1.0, 1.5, 2.0, 3.0 (Low=100, High=200 cố định)	`results/figures/sigma_comparison.png`, dữ liệu trong `results/tables/parameter_results.csv`
EXP-02	Thay đổi cặp Low/High Threshold, giữ nguyên Sigma, quan sát ảnh hưởng đến kết quả Canny.	(50,100), (50,150), (100,200), (100,250), (150,300) (Sigma=1.0 cố định)	`results/figures/threshold_comparison.png`, dữ liệu trong `results/tables/parameter_results.csv`
EXP-03	Đo mật độ biên (edge density) và thời gian xử lý cho từng cấu hình tham số để có căn cứ định lượng khi so sánh, không chỉ quan sát bằng mắt.	Toàn bộ cấu hình của EXP-01, EXP-02	Cột `edge_density_percent`, `processing_time_ms` trong `parameter_results.csv`
EXP-04	Trả lời 6 câu hỏi bắt buộc của đề bài về xu hướng tham số (Sigma tăng/giảm, Low Threshold tăng/giảm, High Threshold tăng/giảm).	Kết quả EXP-01, EXP-02	`docs/06_results/parameter_comparison.md`
EXP-05	Đảm bảo thực nghiệm chạy được ngay cả khi chưa có ảnh thật trong `data/input/normal/` (tự động sinh ảnh mẫu tổng hợp).	Không có ảnh input	Ảnh mẫu được tạo tự động tại `data/input/normal/sample_generated.jpg`
---
3. Tiêu chí hoàn thành (Definition of Done)
[x] Script `parameter_experiment.py` chạy không lỗi bằng lệnh
`python -m src.experiments.parameter_experiment`.
[x] Script `run_experiments.py` hỗ trợ tuỳ chỉnh tham số qua CLI
(`--input`, `--sigma`, `--thresholds`).
[x] Sinh đủ 2 biểu đồ so sánh (`sigma_comparison.png`,
`threshold_comparison.png`) và 1 bảng CSV (`parameter_results.csv`).
[x] Có nhận xét/kết luận bằng văn bản trả lời đầy đủ 6 câu hỏi của đề
trong `parameter_comparison.md`.
[x] Không phụ thuộc dữ liệu ngoài — script tự tạo ảnh mẫu nếu thiếu.
---
4. Phạm vi không thực hiện (Out of Scope)
Các nội dung sau không thuộc phạm vi của TV5, do các thành viên khác phụ trách:
So sánh Canny với Sobel/Laplacian → TV6 (`comparison_experiment.py`).
Chạy Canny trên nhiều loại ảnh (nhiễu, tương phản thấp/cao) → TV6
(`image_type_experiment.py`), TV5 chỉ cung cấp cơ chế thí nghiệm tham số.
So sánh OpenCV vs Scikit-image → TV4 (`opencv_vs_skimage.md`).
