# Test Cases

| ID | Module | Test Case | Input | Expected Result |
|---|---|---|---|---|
| TC01 | Grayscale | Chuyển ảnh sang ảnh xám | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh đầu ra được chuyển sang ảnh xám, đúng kích thước và kiểu dữ liệu |
| TC02 | Gaussian Blur | Làm mờ ảnh bằng Gaussian Blur | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh đầu ra có cùng kích thước với ảnh đầu vào và được làm mờ thành công |
| TC03 | Canny OpenCV | Phát hiện cạnh bằng Canny OpenCV | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh cạnh được tạo thành công, đúng kích thước và kiểu dữ liệu |
| TC04 | Canny Scikit-image | Phát hiện cạnh bằng Canny Scikit-image | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh cạnh được tạo thành công |
| TC05 | Sobel | Phát hiện cạnh bằng Sobel | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh cạnh được tạo thành công |
| TC06 | Laplacian | Phát hiện cạnh bằng Laplacian | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh cạnh được tạo thành công |
| TC07 | Parameter Experiment | Chạy với nhiều giá trị Sigma | Ảnh Normal | Kết quả được tạo đầy đủ cho tất cả các giá trị Sigma được kiểm tra |
| TC08 | Parameter Experiment | Chạy với nhiều cặp Threshold | Ảnh Normal | Kết quả được tạo đầy đủ cho tất cả các cặp Threshold được kiểm tra |
| TC09 | Comparison | So sánh Canny, Sobel và Laplacian | 4 loại ảnh: Normal, Noisy, Low Contrast, High Contrast | Ảnh so sánh được tạo thành công, gồm ảnh gốc và kết quả của 3 thuật toán |
| TC10 | Image Type | Tạo ảnh nhiễu, ảnh tương phản thấp và ảnh tương phản cao | Ảnh Normal | Tạo thành công 3 ảnh: Noisy, Low Contrast và High Contrast |
