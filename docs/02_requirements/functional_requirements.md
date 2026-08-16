# Functional Requirements — Canny Edge Detection

## Yêu cầu chức năng

| Yêu cầu | Mô tả |
|-----------------------------------|----------------------------------------------------------------------------|
| Đọc ảnh đầu vào                   | Đọc được ảnh (.jpg, .png), hỗ trợ ảnh xám và ảnh màu |
| Chuyển ảnh xám                    | Chuyển ảnh màu sang grayscale trước khi xử lý |
| Làm mịn ảnh                       | Áp dụng Gaussian Blur với tham số sigma tùy chỉnh để giảm nhiễu |
| Tính gradient                     | Tính độ lớn và hướng gradient của ảnh |
| Làm mảnh cạnh                     | Loại bỏ điểm không phải cực đại để cạnh mảnh, rõ (Non-Maximum Suppression) |
| Phân loại cạnh                    | Dùng ngưỡng thấp và ngưỡng cao để phân loại cạnh mạnh / cạnh yếu / loại bỏ |
| Nối cạnh yếu                      | Giữ lại cạnh yếu nếu nó liên kết với cạnh mạnh, ngược lại loại bỏ |
| Phát hiện cạnh bằng OpenCV        | Thực hiện Canny bằng hàm `cv2.Canny()` |
| Phát hiện cạnh bằng Scikit-image  | Thực hiện Canny bằng hàm `skimage.feature.canny()` |
| Tùy chỉnh tham số                 | Cho phép thay đổi sigma, ngưỡng thấp, ngưỡng cao để quan sát kết quả |
| So sánh thuật toán                | So sánh Canny với Sobel, Laplacian |
 Xuất kết quả                       | Lưu ảnh cạnh đầu ra và hiển thị so sánh với ảnh gốc |

---

