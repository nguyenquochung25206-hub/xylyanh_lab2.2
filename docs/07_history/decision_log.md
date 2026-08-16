# Decision Log — xylyanh_lab2.2

Ghi lại các quyết định kỹ thuật quan trọng và lý do đằng sau, để tránh
tranh cãi lặp lại và giúp thành viên hiểu vì sao code được tổ chức như vậy

---

### QĐ-01: Mỗi thuật toán biên tự làm tiền xử lý bên trong (không tách riêng bước preprocessing ở main.py)

**Bằng chứng:** `canny_opencv.py`, `sobel.py`, `laplacian.py` đều tự gọi
`convert_to_grayscale()` và `apply_gaussian_blur()` bên trong hàm
`detect_edges()`, thay vì để `main.py` gọi trước rồi truyền ảnh đã xử lý vào.

**Hệ quả:** `main.py` chỉ cần đọc ảnh gốc và gọi đúng 1 hàm `detect_edges()`
tương ứng — không được tự ý grayscale/blur trước, nếu không ảnh sẽ bị xử lý
2 lần và làm sai lệch kết quả thí nghiệm sigma/threshold. Đây là lỗi thật
TV1 từng gặp phải khi tích hợp `main.py` (đã sửa ngày 2026-08-16).

---

### QĐ-02: Dùng import tuyệt đối `from src.xxx import yyy`, bắt buộc chạy qua `python -m src.main`

**Bằng chứng:** Commit `Refactor import path for detect_edges function`
(lelanmy1209-tech, 2026-08-15) đổi toàn bộ import trong file test sang dạng
`from src.edge_detection.canny_opencv import detect_edges`. Toàn bộ code
trong `edge_detection/` (canny_opencv.py, sobel.py, laplacian.py) cũng dùng
`from src.preprocessing.grayscale import convert_to_grayscale`.

**Hệ quả:** Không thể chạy `python src/main.py` trực tiếp từ trong thư mục
`src/` (sẽ báo lỗi `ModuleNotFoundError: No module named 'src'`). Bắt buộc
chạy từ thư mục gốc repo bằng `python -m src.main`. Toàn bộ thành viên cần
tuân theo quy ước import này khi viết thêm module mới, để không lặp lại lỗi
tương tự lỗi `main.py` gặp trước đó (import sai `preprocessing.grayscale`
thay vì `src.preprocessing.grayscale`).

---

### QĐ-03: Tên hàm trả về ảnh biên thống nhất là `detect_edges()` (trừ Scikit-image)

**Bằng chứng:** `canny_opencv.py`, `sobel.py`, `laplacian.py` đều export hàm
tên `detect_edges(image, ...)`. Riêng `canny_skimage.py` export hàm tên
`canny_skimage(image, ...)` (không theo quy ước chung).

**Hệ quả:** Khi gọi 3 hàm đầu, `main.py`/`experiments/` có thể dùng chung
một alias khi import (`from ... import detect_edges as canny_opencv`). Với
Scikit-image phải import riêng theo đúng tên `canny_skimage`, và ảnh đầu
vào cần đổi từ BGR (do `cv2.imread` trả về) sang RGB trước khi gọi, vì hàm
này dùng `skimage.color.rgb2gray()` bên trong (kỳ vọng thứ tự kênh RGB).
Nếu bỏ qua bước đổi kênh này, trọng số grayscale sẽ bị lệch (đổi chỗ kênh đỏ
và xanh dương), khiến so sánh kết quả OpenCV vs Scikit-image không công
bằng — đây là lỗi tiềm ẩn TV1 phát hiện khi tích hợp `main.py`, đã sửa ngày
2026-08-16.

---

### QĐ-04: Lưu ảnh kết quả tập trung qua `save_results.py` thay vì mỗi module tự gọi `cv2.imwrite()`

**Bằng chứng:** `main.py` và các module trong `src/experiments/` đều gọi
`save_result(edges, output_path)` từ `src/visualization/save_results.py`
thay vì gọi `cv2.imwrite()` trực tiếp.

**Hệ quả:** Đảm bảo mọi nơi trong project lưu ảnh theo cùng chuẩn (tự tạo
thư mục cha nếu chưa có, báo lỗi rõ ràng nếu ghi thất bại). Nếu cần đổi định
dạng lưu (ví dụ thêm log, đổi sang .jpg) chỉ cần sửa một chỗ.

---

### QĐ-05: (điền quyết định tiếp theo khi phát sinh, ghi ngày thật)

**Ngày:**
**Bối cảnh:**
**Quyết định:**
**Hệ quả:**
