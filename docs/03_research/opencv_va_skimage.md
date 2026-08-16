## So sánh chi tiết Canny Edge Detection: OpenCV vs Scikit-image
# 1. Tổng quan về Canny Edge Detection
* Canny Edge Detection là thuật toán phát hiện biên tối ưu, gồm 5 bước chính:

* Giảm nhiễu: dùng Gaussian blur để làm mịn ảnh.

* Tính gradient: dùng Sobel (hoặc phương pháp khác) để tính độ lớn và hướng gradient.

* Non-maximum suppression: giữ lại các pixel có gradient cực đại trên hướng gradient, loại bỏ pixel không phải biên.

* Double threshold: phân loại pixel thành biên mạnh, biên yếu và không phải biên dựa trên hai ngưỡng (low/high).

* Hysteresis edge tracking: kết nối biên yếu với biên mạnh để tạo thành đường biên liên tục.
# 2. Canny trong OpenCV (cv2.Canny)
edges = cv2.Canny(image, threshold1, threshold2, apertureSize=3, L2gradient=False)
* image: ảnh đầu vào (grayscale, uint8).

* threshold1: ngưỡng thấp (low threshold).

* threshold2: ngưỡng cao (high threshold).

* apertureSize: kích thước kernel Sobel (mặc định 3).

* L2gradient: nếu True thì dùng L2 norm (sqrt(gx²+gy²)), mặc định False (L1 norm = |gx|+|gy|).

* Cách hoạt động:
Gaussian blur: OpenCV tự động áp dụng bộ lọc Gaussian bên trong với kích thước kernel được tính từ apertureSize (thường là 5x5). Bạn không điều chỉnh sigma trực tiếp, nhưng có thể làm mờ trước nếu muốn.

Ngưỡng: threshold1 và threshold2 là giá trị tuyệt đối (0–255). Nếu một pixel có gradient > threshold2 thì là biên mạnh, nếu < threshold1 thì loại bỏ, nếu ở giữa thì là biên yếu (sẽ được xem xét kết nối).

Hysteresis: mặc định có sẵn.

* Ưu điểm:
Nhanh, tối ưu cho C++ và embedded.

Ít tham số, dễ dùng.

* Nhược điểm:
Không kiểm soát được sigma Gaussian một cách trực tiếp.

Ngưỡng tuyệt đối nhạy cảm với ảnh khác nhau (cần điều chỉnh thủ công).
# 3. Canny trong Scikit-image (skimage.feature.canny)
edges = feature.canny(image, sigma=1.0, low_threshold=None, high_threshold=None, use_quantiles=False, mask=None)
* image: ảnh grayscale, float trong [0,1] (hoặc sẽ tự chuyển).

* sigma: độ lệch chuẩn của Gaussian blur (mặc định 1.0).

* low_threshold: ngưỡng thấp (tỷ lệ so với giá trị gradient cực đại, từ 0 đến 1).

* high_threshold: ngưỡng cao (tương tự).

* use_quantiles: nếu True, low/high được hiểu là phân vị (quantile) của gradient magnitude.

* mask: mặt nạ nhị phân để chỉ định vùng tính biên.

* Cách hoạt động:
Gaussian blur: bạn có thể điều chỉnh trực tiếp sigma, ảnh hưởng đến mức độ làm mịn.

Ngưỡng: low_threshold và high_threshold là tỷ lệ so với giá trị gradient lớn nhất. Ví dụ: nếu gradient max = 100, low=0.1 → 10, high=0.2 → 20. Điều này giúp ngưỡng tự động thích ứng với từng ảnh.

Hysteresis: tích hợp sẵn.

* Ưu điểm:
Kiểm soát tốt sigma và ngưỡng theo tỷ lệ, dễ điều chỉnh.

Phù hợp với nghiên cứu và xử lý ảnh khoa học.

* Nhược điểm:
Chậm hơn OpenCV (do Python + NumPy).

Yêu cầu ảnh float [0,1], dễ gây lỗi nếu không chuyển đổi đúng.
# 4. So sánh chi tiết giữa OpenCV và Scikit-image
* 4.1 Tham số và cách đặt ngưỡng
| Tham số          | OpenCV                                                            | Scikit-image                        |
| ---------------- | ----------------------------------------------------------------- |-------------------------------------|
| Gaussian sigma   | Không có tham số riêng, dùng kernel cố định (tính từ apertureSize)| Có sigma, điều chỉnh mức độ làm mịn |
| Ngưỡng thấp (low)| Giá trị tuyệt đối (0-255)	                                       | Tỷ lệ (0-1) so với gradient max     |  
| Ngưỡng cao (high)| Giá trị tuyệt đối (0-255)                                         | Tỷ lệ (0-1) so với gradient max     |
| Hysteresis       | Tự động                                                           | Tự động                             |
| Sobel kernel size| apertureSize (3,5,7)                                              | Mặc định 3 (không thay đổi)         |
| L2 gradient      | Tùy chọn (L2gradient)                                             | Luôn dùng L2 norm                   |
Giải thích ý nghĩa:

Với OpenCV, nếu bạn có ảnh sáng hơn (giá trị pixel cao), gradient cũng cao hơn, bạn cần tăng threshold tương ứng. Nếu chuyển sang ảnh khác, bạn phải thử lại.

Với Scikit-image, ngưỡng là tỷ lệ, nên dù ảnh sáng hay tối, nếu đặt low=0.1, nó sẽ tự tính low = 10% của gradient max. Giúp nhất quán hơn khi thử nghiệm.
* 4.2 Xử lý Gaussian blur
OpenCV: áp dụng bộ lọc Gaussian với kích thước kernel = 2*int(2*sigma)+1 (tính từ apertureSize nếu bạn không tự làm mờ trước). Thực tế, bạn có thể tự làm mờ rồi mới gọi Canny để kiểm soát sigma.

Scikit-image: tích hợp sigma trực tiếp, dễ dàng thay đổi để thấy ảnh hưởng của làm mờ.
* 4.3 Kết quả thực tế trên ảnh Panda
Dựa trên bộ ảnh bạn đã chạy (với sigma=1.0, low=0.1, high=0.2 cho skimage; và OpenCV dùng low=100, high=200):
| Loại ảnh      | OpenCV (100, 200)                     | Scikit-image (sigma=1, low=0.1, high=0.2)  |
| ------------- | ------------------------------------- |--------------------------------------------|
| Normal        | Biên sắc nét, ít nhiễu                | Biên mảnh hơn, giữ chi tiết nhỏ            |
| Noisy         | Nhiễu nhiều, biên bị lẫn	            | Nhiễu ít hơn (do sigma làm mờ), biên rõ hơn|  
| Low contrast  | Mất nhiều biên yếu, chỉ giữ biên mạnh | Giữ được biên yếu tốt hơn                  |
| High contrast | Biên rất rõ, có thể bị tràn           | Biên ổn định, không bị bão hòa             |
Nhận xét: OpenCV thường cho biên đậm hơn nhưng dễ mất chi tiết với ảnh low contrast. Scikit-image với tỷ lệ ngưỡng thích ứng tốt hơn nhưng có thể thừa chi tiết không mong muốn.
* 4.4 Hiệu suất
Đo thử trên ảnh 512x512:

OpenCV: ~2-3 ms

Scikit-image: ~15-20 ms
→ OpenCV phù hợp ứng dụng real-time, còn skimage phù hợp nghiên cứu và phân tích.
# 5 Tình huống sài OpenCV và Skimage
* Nên dùng OpenCV khi:
Ứng dụng yêu cầu tốc độ (video, real-time).

Bạn đã biết ngưỡng tuyệt đối phù hợp với ảnh của bạn.

Cần tích hợp với các hàm xử lý ảnh khác của OpenCV (phép biến đổi, contour, ...).

* Nên dùng Scikit-image khi:
Bạn đang trong giai đoạn thí nghiệm, cần thay đổi tham số nhanh.

Ảnh đầu vào có độ sáng/chất lượng khác nhau, cần ngưỡng thích ứng.

Bạn muốn kết hợp với SciPy và các công cụ khoa học khác.
# 6. Hướng dẫn chuyển đổi tham số giữa hai thư viện
* Để so sánh công bằng, bạn có thể ước lượng:

Với ảnh uint8, gradient max ≈ 255.

* Chuyển từ skimage sang OpenCV:

low_abs = low_ratio * 255

high_abs = high_ratio * 255

* Chuyển từ OpenCV sang skimage:

low_ratio = low_abs / 255

high_ratio = high_abs / 255

Tuy nhiên, đây chỉ là xấp xỉ vì cách tính gradient và làm mờ khác nhau. Tốt nhất là thử nghiệm trực tiếp.
# 7. Kết luận
OpenCV và Scikit-image đều triển khai Canny tốt, nhưng với cách tiếp cận khác nhau.

OpenCV mạnh về hiệu năng, ít tham số, phù hợp với ứng dụng thực tế.

Scikit-image cung cấp nhiều tùy biến, dễ điều chỉnh cho nghiên cứu và so sánh.

Khi viết báo cáo, cần chỉ rõ tham số đã dùng và nhận xét sự khác biệt dựa trên quan sát cụ thể.
