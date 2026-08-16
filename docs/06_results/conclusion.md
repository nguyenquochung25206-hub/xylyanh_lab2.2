# Conclusion

## 1. Tổng quan

Project đã xây dựng và kiểm thử hệ thống phát hiện cạnh ảnh bằng thuật toán Canny.

Hệ thống gồm:

- Canny OpenCV
- Canny Scikit-image
- Thí nghiệm thay đổi Sigma
- Thí nghiệm thay đổi Threshold
- So sánh Canny với Sobel và Laplacian
- Kiểm thử trên nhiều loại ảnh

---

## 2. Kết quả kiểm thử

Các module chính đã được kiểm thử bằng Pytest.

Kết quả:

| Module | Kết quả |
|---|---|
| Grayscale | PASS |
| Gaussian Blur | PASS |
| Canny OpenCV | PASS |
| Canny Scikit-image | PASS |
| Parameter Experiment | PASS |
| Sobel | PASS |
| Laplacian | PASS |
| Image Type Experiment | PASS |
| Comparison Experiment | PASS |
| Pipeline | PASS |

Các test kiểm tra khả năng xử lý ảnh, kích thước output, kiểu dữ liệu, kết quả phát hiện cạnh và khả năng chạy các thí nghiệm.

---

## 3. Canny OpenCV

Canny OpenCV được xây dựng theo pipeline:

Input Image → Grayscale → Gaussian Blur → Canny → Edge Image.

Kết quả kiểm thử cho thấy pipeline hoạt động đúng và tạo được ảnh cạnh.

Ảnh đầu ra có cùng kích thước với ảnh đầu vào và sử dụng kiểu dữ liệu phù hợp.

---

## 4. Canny Scikit-image

Canny Scikit-image cũng hoạt động đúng trên ảnh đầu vào.

Kết quả đầu ra là ảnh cạnh hai chiều và có cùng kích thước với ảnh gốc.

Việc kiểm thử giúp đảm bảo module có thể thực hiện phát hiện cạnh độc lập với phiên bản OpenCV.

---

## 5. Ảnh hưởng của Sigma

Thí nghiệm Sigma được thực hiện với nhiều giá trị khác nhau:

- 0.5
- 1.0
- 1.5
- 2.0
- 3.0

Sigma được sử dụng trong Gaussian Blur.

Khi Sigma tăng, mức độ làm mờ ảnh tăng. Điều này có thể làm giảm nhiễu và các chi tiết nhỏ trước khi thực hiện Canny.

Tuy nhiên, nếu Sigma quá lớn, một số cạnh nhỏ hoặc chi tiết có thể bị làm mờ và khó phát hiện.

---

## 6. Ảnh hưởng của Threshold

Thí nghiệm Threshold được thực hiện với nhiều cặp giá trị Low Threshold và High Threshold.

Threshold ảnh hưởng trực tiếp đến việc xác định cạnh mạnh và cạnh yếu trong thuật toán Canny.

Threshold thấp có thể phát hiện nhiều cạnh hơn nhưng cũng có khả năng tạo thêm cạnh giả.

Threshold cao giúp loại bỏ nhiều cạnh yếu và tập trung vào các cạnh mạnh.

---

## 7. So sánh các thuật toán

Project thực hiện so sánh:

- Canny
- Sobel
- Laplacian

Các thuật toán cho kết quả khác nhau về khả năng phát hiện cạnh và mức độ ảnh hưởng của nhiễu.

Canny có quy trình xử lý nhiều bước nên có khả năng kiểm soát cạnh tốt hơn trong nhiều trường hợp.

Sobel và Laplacian có cách tính gradient khác nhau và có thể cho kết quả khác với Canny.

---

## 8. Kiểm thử nhiều loại ảnh

Hệ thống được kiểm thử trên:

- Normal
- Noisy
- Low Contrast
- High Contrast

Việc sử dụng nhiều loại ảnh giúp đánh giá khả năng hoạt động của thuật toán trong các điều kiện đầu vào khác nhau.

Ảnh nhiễu có thể tạo thêm nhiều cạnh không mong muốn.

Ảnh tương phản thấp có thể làm một số cạnh khó phát hiện.

Ảnh tương phản cao thường giúp các cạnh rõ ràng hơn.

---

## 9. Đánh giá chung

Hệ thống đáp ứng các yêu cầu chính của bài Lab:

- Tiền xử lý ảnh.
- Phát hiện cạnh bằng Canny.
- Sử dụng OpenCV.
- Sử dụng Scikit-image.
- Thử nghiệm Sigma.
- Thử nghiệm Threshold.
- So sánh với Sobel và Laplacian.
- Kiểm thử trên nhiều loại ảnh.
- Tự động kiểm thử bằng Pytest.

Các module chính đều vượt qua các test case đã xây dựng.

---

## 10. Kết luận

Qua quá trình xây dựng và kiểm thử, project cho thấy thuật toán Canny có thể được sử dụng hiệu quả để phát hiện cạnh trong ảnh.

Các tham số như Sigma, Low Threshold và High Threshold có ảnh hưởng đáng kể đến kết quả phát hiện cạnh.

Việc kết hợp tiền xử lý, thử nghiệm nhiều tham số và kiểm thử trên nhiều loại ảnh giúp đánh giá hệ thống toàn diện hơn.

Project đã hoàn thành các chức năng và yêu cầu chính của bài Lab.
