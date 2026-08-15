Experiment Log - TV3 OpenCV
1. Thông tin
Thành viên: TV3
Module: OpenCV Canny Edge Detector
Thư viện: OpenCV
Hàm chính: `cv2.Canny()`
---
2. Pipeline
Input Image
→ Grayscale
→ Gaussian Blur
→ Canny
→ Output Edge Image
---
3. Experiment 1 - Ảnh bình thường
Input
Sử dụng 5 ảnh:
normal_01.jpg
normal_02.jpg
normal_03.jpg
normal_04.jpg
normal_05.jpg
Parameters
Gaussian Kernel: (5, 5)
Sigma: 1.0
Low Threshold: 100
High Threshold: 200
Nhận xét
Canny phát hiện được các đường biên chính
của các đối tượng trong ảnh.
---
4. Experiment 2 - Ảnh nhiễu
Input
Sử dụng các ảnh trong:
`data/input/noisy/`
Parameters
Gaussian Kernel: (5, 5)
Sigma: 1.0
Low Threshold: 100
High Threshold: 200
Nhận xét
Ảnh nhiễu có thể tạo ra nhiều cạnh không mong muốn.
Gaussian Blur giúp giảm ảnh hưởng của nhiễu
trước khi thực hiện thuật toán Canny.
---
5. Experiment 3 - Thay đổi Threshold
STT	Low	High
1	50	100
2	50	150
3	100	200
4	100	250
5	150	300
Nhận xét
Khi threshold thấp, Canny có xu hướng phát hiện
nhiều cạnh hơn.
Khi threshold cao, các cạnh yếu có thể bị loại bỏ.
Giá trị 100/200 được sử dụng làm cấu hình mặc định
cho các thí nghiệm ban đầu.
---
6. Kết luận
Thí nghiệm cho thấy kết quả Canny phụ thuộc đáng kể
vào các tham số threshold và sigma.
Gaussian Blur giúp giảm nhiễu trước khi phát hiện cạnh.
Việc lựa chọn threshold phù hợp giúp cân bằng giữa
việc phát hiện đủ cạnh và hạn chế các cạnh giả.
---
7. Experiment Log - TV5 Parameter Experiment
7.1. Thông tin
Thành viên: TV5
Module: `src/experiments/parameter_experiment.py`
Script chạy: `src/scripts/run_experiments.py`
Mục tiêu: Định lượng ảnh hưởng của Sigma và Threshold đến kết quả Canny.
7.2. Ghi chú kỹ thuật
Trong quá trình triển khai phát hiện `data/input/normal/` chưa có ảnh thật
(thư mục trống). Để đảm bảo pipeline luôn chạy được ngay cả khi chưa có bộ
ảnh chính thức, TV5 đã bổ sung cơ chế tự động tạo ảnh mẫu tổng hợp
(`create_sample_image()`, seed cố định = 42) khi không tìm thấy ảnh nào
trong thư mục input. Khi TV3 bổ sung ảnh thật vào `data/input/normal/`,
script sẽ tự động ưu tiên dùng ảnh thật ở lần chạy tiếp theo mà không cần
sửa code.
7.3. Experiment EXP-01 - Thay đổi Sigma
Cố định Low=100, High=200. Kết quả cho thấy mật độ biên giảm dần khi
Sigma tăng từ 0.5 đến 2.0 (1.932% → 1.772%), do ảnh bị làm mờ mạnh hơn.
7.4. Experiment EXP-02 - Thay đổi Threshold
Cố định Sigma=1.0. Mật độ biên giữ ổn định ở các threshold thấp/trung
bình và giảm rõ rệt khi threshold tăng mạnh lên (150, 300), do nhiều biên
yếu không còn đủ điều kiện được giữ lại theo Hysteresis.
7.5. Kết quả đầy đủ
Xem chi tiết tại `docs/06_results/parameter_comparison.md` và dữ liệu thô
tại `results/tables/parameter_results.csv`.
