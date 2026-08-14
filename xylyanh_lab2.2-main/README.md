# Image Processing Lab 02 – Canny Edge Detection

## 1. Giới thiệu

Project **Image Processing Lab 02 – Canny Edge Detection** tập trung vào việc tìm hiểu và triển khai các thuật toán phát hiện biên ảnh (Edge Detection).

Thuật toán **Canny** được triển khai và so sánh giữa hai thư viện **OpenCV** và **Scikit-image**. Ngoài ra, project còn so sánh Canny với hai phương pháp phát hiện biên phổ biến là **Sobel** và **Laplacian**.

Các thuật toán được đánh giá trên nhiều loại ảnh khác nhau, bao gồm:

* Ảnh bình thường (Normal)
* Ảnh có nhiễu (Noisy)
* Ảnh tương phản thấp (Low Contrast)
* Ảnh tương phản cao (High Contrast)

---

## 2. Mục tiêu

Project được thực hiện nhằm:

* Tìm hiểu cơ sở lý thuyết của thuật toán Canny.
* Hiểu rõ từng bước trong quy trình Canny Edge Detection.
* Triển khai Canny bằng OpenCV.
* Triển khai Canny bằng Scikit-image.
* Phân tích ảnh hưởng của các tham số đến kết quả.
* So sánh Canny với Sobel và Laplacian.
* Đánh giá thuật toán trên nhiều loại ảnh.
* Trực quan hóa và lưu trữ kết quả thực nghiệm.
* Kiểm thử các thành phần chính của project.

---

## 3. Các thuật toán

### 3.1. Canny Edge Detection

Thuật toán Canny gồm các bước chính:

```text
Input Image
     ↓
Grayscale
     ↓
Gaussian Blur
     ↓
Gradient Calculation
     ↓
Non-Maximum Suppression
     ↓
Double Threshold
     ↓
Edge Tracking by Hysteresis
     ↓
Output Edge Image
```

### 3.2. Sobel

Sobel sử dụng đạo hàm bậc nhất theo hai hướng ngang và dọc để xác định những vùng có sự thay đổi cường độ lớn trong ảnh.

### 3.3. Laplacian

Laplacian sử dụng đạo hàm bậc hai để phát hiện những vùng có sự thay đổi cường độ mạnh trong ảnh.

---

## 4. Thư viện và công nghệ

Project sử dụng:

| Công nghệ        | Mục đích                 |
| ---------------- | ------------------------ |
| Python           | Ngôn ngữ lập trình chính |
| OpenCV           | Xử lý ảnh và Canny       |
| Scikit-image     | Triển khai Canny         |
| NumPy            | Xử lý dữ liệu số         |
| Matplotlib       | Trực quan hóa kết quả    |
| Jupyter Notebook | Thử nghiệm và phân tích  |
| Pytest           | Kiểm thử                 |

---

## 5. Cài đặt

### 5.1. Tạo môi trường ảo

```bash
python -m venv venv
```

### 5.2. Kích hoạt môi trường ảo

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 5.3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## 6. Cách chạy

### Chạy chương trình chính

```bash
python src/main.py
```

### Chạy Canny

```bash
python scripts/run_canny.py
```

### Chạy các thí nghiệm

```bash
python scripts/run_experiments.py
```

### Chạy kiểm thử

```bash
pytest
```

---

## 7. Dữ liệu thực nghiệm

Project sử dụng bốn nhóm ảnh đầu vào:

| Loại ảnh         | Mô tả                                   |
| ---------------- | --------------------------------------- |
| `normal/`        | Ảnh bình thường, ít hoặc không có nhiễu |
| `noisy/`         | Ảnh có nhiễu                            |
| `low_contrast/`  | Ảnh có độ tương phản thấp               |
| `high_contrast/` | Ảnh có độ tương phản cao                |

Cấu trúc dữ liệu:

```text
data/
├── input/
│   ├── normal/
│   ├── noisy/
│   ├── low_contrast/
│   └── high_contrast/
│
├── output/
│   ├── opencv/
│   ├── skimage/
│   └── comparison/
│
└── sample/
```

---

## 8. Các thực nghiệm

### Experiment 1 – Canny OpenCV vs Scikit-image

So sánh kết quả phát hiện biên khi sử dụng:

```text
Canny OpenCV
      ↕
Canny Scikit-image
```

Mục tiêu là đánh giá sự khác biệt về kết quả khi sử dụng hai thư viện.

### Experiment 2 – Phân tích tham số

Thay đổi các tham số của Canny để đánh giá ảnh hưởng đến kết quả:

* Gaussian sigma
* Low threshold
* High threshold

Kết quả được trực quan hóa và lưu lại để so sánh.

### Experiment 3 – So sánh thuật toán

So sánh:

```text
Canny
  ↕
Sobel
  ↕
Laplacian
```

Các kết quả được đánh giá dựa trên khả năng phát hiện biên, độ rõ của biên và mức độ ảnh hưởng của nhiễu.

### Experiment 4 – Ảnh hưởng của loại ảnh

Thực hiện trên:

```text
Normal
   ↓
Noisy
   ↓
Low Contrast
   ↓
High Contrast
```

Mục tiêu là đánh giá khả năng hoạt động của thuật toán Canny trong những điều kiện ảnh khác nhau.

---

## 9. Cấu trúc project

```text
ImageProcessing_Lab02_Canny/
│
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── requirements.txt
│
├── docs/
│   ├── 01_project_management/
│   │   ├── project_plan.md
│   │   ├── project_roadmap.md
│   │   ├── task_list.md
│   │   ├── timeline.md
│   │   └── meeting_notes.md
│   │
│   ├── 02_requirements/
│   │   ├── lab_requirements.md
│   │   ├── functional_requirements.md
│   │   └── experiment_requirements.md
│   │
│   ├── 03_research/
│   │   ├── canny_theory.md
│   │   ├── canny_algorithm.md
│   │   ├── parameter_analysis.md
│   │   ├── sobel_vs_laplacian_vs_canny.md
│   │   └── applications.md
│   │
│   ├── 04_design/
│   │   ├── system_architecture.md
│   │   ├── processing_pipeline.md
│   │   └── diagrams/
│   │       ├── system_flow.png
│   │       └── canny_pipeline.png
│   │
│   ├── 05_testing/
│   │   ├── test_plan.md
│   │   ├── test_cases.md
│   │   └── test_report.md
│   │
│   ├── 06_results/
│   │   ├── experiment_results.md
│   │   ├── parameter_comparison.md
│   │   └── conclusion.md
│   │
│   └── 07_history/
│       ├── changelog.md
│       ├── decision_log.md
│       ├── experiment_log.md
│       └── ai_usage_log.md
│
├── data/
│   ├── input/
│   │   ├── normal/
│   │   ├── noisy/
│   │   ├── low_contrast/
│   │   └── high_contrast/
│   │
│   ├── output/
│   │   ├── opencv/
│   │   ├── skimage/
│   │   └── comparison/
│   │
│   └── sample/
│
├── src/
│   ├── __init__.py
│   │
│   ├── preprocessing/
│   │   ├── __init__.py
│   │   ├── grayscale.py
│   │   └── gaussian_blur.py
│   │
│   ├── edge_detection/
│   │   ├── __init__.py
│   │   ├── canny_opencv.py
│   │   ├── canny_skimage.py
│   │   ├── sobel.py
│   │   └── laplacian.py
│   │
│   ├── experiments/
│   │   ├── parameter_experiment.py
│   │   ├── image_type_experiment.py
│   │   └── comparison_experiment.py
│   │
│   ├── visualization/
│   │   ├── display_results.py
│   │   ├── plot_comparison.py
│   │   └── save_results.py
│   │
│   └── main.py
│
├── tests/
│   ├── test_canny_opencv.py
│   ├── test_canny_skimage.py
│   ├── test_parameters.py
│   └── test_pipeline.py
│
├── notebooks/
│   ├── 01_canny_basic.ipynb
│   ├── 02_parameter_analysis.ipynb
│   └── 03_algorithm_comparison.ipynb
│
├── scripts/
│   ├── run_canny.py
│   ├── run_experiments.py
│   └── generate_report.py
│
└── results/
    ├── figures/
    ├── tables/
    └── reports/
```

---

## 10. Kết quả

Các kết quả thực nghiệm được lưu trữ theo nhóm:

```text
results/
├── figures/
├── tables/
└── reports/
```

Ảnh kết quả từ các thuật toán được lưu tại:

```text
data/output/
├── opencv/
├── skimage/
└── comparison/
```

Các kết quả bao gồm:

* Ảnh biên từ Canny OpenCV.
* Ảnh biên từ Canny Scikit-image.
* Kết quả Sobel.
* Kết quả Laplacian.
* So sánh ảnh hưởng của tham số.
* So sánh trên các loại ảnh khác nhau.
* Bảng và biểu đồ kết quả.

---

## 11. Testing

Project sử dụng **Pytest** để kiểm thử các thành phần chính.

Các nhóm kiểm thử gồm:

* Kiểm thử Canny OpenCV.
* Kiểm thử Canny Scikit-image.
* Kiểm thử tham số.
* Kiểm thử toàn bộ pipeline.

Chạy toàn bộ test:

```bash
pytest
```

---

## 12. Tài liệu

Các tài liệu của project được tổ chức trong thư mục `docs/`, bao gồm:

* Quản lý project.
* Yêu cầu project.
* Nghiên cứu lý thuyết.
* Thiết kế hệ thống.
* Kiểm thử.
* Kết quả thực nghiệm.
* Lịch sử phát triển project.

---

## 13. License

Project được phát triển cho mục đích học tập trong khuôn khổ **Image Processing Lab 02**.
