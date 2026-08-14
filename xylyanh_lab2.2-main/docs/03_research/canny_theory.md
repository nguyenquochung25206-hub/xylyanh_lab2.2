## 1. Canny là gì?
Canny Edge Detector là một thuật toán phát hiện biên (edge detection) do John F. Canny đề xuất năm 1986. Đây được xem là một trong những thuật toán phát hiện biên kinh điển và hiệu quả nhất trong xử lý ảnh, vì nó được xây dựng dựa trên ba tiêu chí tối ưu mà Canny đặt ra:
    • Tỷ lệ phát hiện lỗi thấp (Good detection): thuật toán phải phát hiện được càng nhiều cạnh thật càng tốt, đồng thời hạn chế tối đa việc bỏ sót cạnh hoặc tạo ra cạnh giả.
    • Định vị chính xác (Good localization): vị trí cạnh được phát hiện phải càng gần vị trí cạnh thật trong ảnh gốc càng tốt.
    • Phản hồi một lần cho một cạnh (Minimal response): mỗi cạnh thật chỉ nên được đánh dấu một lần (đường mảnh, không lặp lại nhiều điểm cho cùng một cạnh).
Khác với các toán tử phát hiện biên đơn giản (chỉ dựa trên đạo hàm bậc một hoặc bậc hai của cường độ ảnh như Sobel, Laplacian), Canny là một quy trình nhiều bước (multi-stage algorithm), kết hợp làm mịn ảnh, tính gradient, triệt tiêu không cực đại và ngưỡng kép có trễ để cho ra các đường biên mảnh, liên tục và ít nhiễu.


## 7. Ưu điểm
    • Cho cạnh mảnh (1 pixel), rõ ràng và liên tục nhờ bước Non-Maximum Suppression.
    • Khả năng chống nhiễu tốt nhờ bước làm mịn Gaussian ở đầu vào.
    • Ngưỡng kép kết hợp hysteresis giúp giữ lại các đoạn cạnh yếu nhưng thật, đồng thời loại bỏ hiệu quả các điểm nhiễu rời rạc.
    • Được xây dựng dựa trên tiêu chí tối ưu toán học rõ ràng (phát hiện tốt, định vị chính xác, phản hồi một lần) nên hiệu quả và ổn định hơn các toán tử đơn giản.
    • Có thể tinh chỉnh linh hoạt qua các tham số σ, ngưỡng thấp/cao để phù hợp với từng loại ảnh.

## 8. Nhược điểm
    • Chi phí tính toán cao hơn (nhiều bước xử lý) so với Sobel, Laplacian → chậm hơn, khó áp dụng thời gian thực trên thiết bị hạn chế tài nguyên.
    • Nhạy cảm với việc lựa chọn tham số (σ, ngưỡng thấp/cao): tham số không phù hợp có thể làm mất cạnh thật hoặc sinh cạnh giả.
    • Không có khả năng tự động thích nghi ngưỡng theo từng vùng ảnh (ngưỡng cố định cho toàn ảnh), nên hoạt động kém với ảnh có độ tương phản không đồng đều.
    • Kết quả là ảnh nhị phân (cạnh có/không) nên có thể mất thông tin về cường độ/độ tin cậy của từng cạnh.