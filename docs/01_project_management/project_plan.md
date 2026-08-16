# Kế hoạch Project — Lab 02: Canny Edge Detection

## 1. Mục tiêu project

Xây dựng một hệ thống hoàn chỉnh triển khai và đánh giá thuật toán Canny Edge Detection, đáp ứng các yêu cầu của đề bài Lab 02, bao gồm: cài đặt bằng OpenCV và Scikit-image, thực nghiệm tham số, so sánh với các thuật toán phát hiện biên khác, và tổng hợp báo cáo kết quả.

## 2. Phạm vi (Scope)

**Bao gồm:**
- Tiền xử lý ảnh (grayscale, Gaussian blur).
- Cài đặt Canny bằng OpenCV (`cv2.Canny`) và Scikit-image (`skimage.feature.canny`).
- So sánh Canny với Sobel và Laplacian.
- Thực nghiệm ảnh hưởng của Sigma và Threshold (low/high).
- Áp dụng trên 4 loại ảnh: bình thường, nhiễu, tương phản thấp, tương phản cao.
- Kiểm thử pipeline và tổng hợp báo cáo kết quả.

**Không bao gồm:**
- Xây dựng thuật toán Canny từ đầu (from scratch) không dùng thư viện — trừ khi đề bài yêu cầu bổ sung.
- Ứng dụng thực tế ngoài phạm vi ảnh tĩnh (video, real-time) — trừ khi được thống nhất mở rộng thêm.

## 3. Thành viên & vai trò

| Thành viên | Vai trò | Nhiệm vụ chính |
|---|---|---|
| TV1 | Project Manager / System Integration | Quản lý project, kiến trúc, tích hợp toàn bộ code |
| TV2 | Canny Researcher | Nghiên cứu thuật toán Canny và cơ sở lý thuyết |
| TV3 | OpenCV Developer | Canny bằng OpenCV + tiền xử lý |
| TV4 | Scikit-image Developer | Canny bằng Scikit-image + phân tích khác biệt |
| TV5 | Parameter Experiment | Thí nghiệm Sigma + Threshold |
| TV6 | Algorithm & Image Comparison | Sobel/Laplacian + nhiều loại ảnh |
| TV7 | Testing + Results | Testing, tổng hợp kết quả, kết luận, báo cáo |

## 4. Luồng làm việc

```
                    TV1
             Project Management
                    │
        ┌───────────┴───────────┐
        ↓                       ↓
      TV2                     TV3
   Canny Theory           Preprocessing
        │                       │
        │                       ↓
        │                      TV4
        │                 Scikit-image
        │                       │
        └───────────┬───────────┘
                    ↓
                  TV5
             Parameter Test
                    │
                    ↓
                  TV6
        Algorithm + Image Comparison
                    │
                    ↓
                  TV7
          Testing + Final Results
                    │
                    ↓
                  TV1
             Final Integration
```

Nguyên tắc: giao việc theo **ownership của module/file**, không tách rời kiểu "người viết code, người viết tài liệu". Mỗi thành viên chịu trách nhiệm từ code → test → tài liệu → commit của module mình phụ trách.

## 5. Mốc thời gian tổng quan

Xem chi tiết tại `timeline.md` và `project_roadmap.md`.

## 6. Rủi ro & phương án xử lý

| Rủi ro | Ảnh hưởng | Phương án |
|---|---|---|
| TV3/TV4 chậm tiến độ, TV1 không có module để tích hợp | Trễ main.py, trễ toàn bộ pipeline | TV1 theo dõi tiến độ hàng tuần, viết interface/placeholder trước để các module khác không bị chặn |
| Kết quả OpenCV và Scikit-image chênh lệch lớn, khó lý giải | Ảnh hưởng chất lượng phân tích | TV4 phối hợp TV2 đối chiếu lại cách hai thư viện xử lý tham số (sigma vs. threshold tuyệt đối) |
| Dữ liệu ảnh đầu vào không đại diện đủ 4 loại | Kết luận thí nghiệm thiếu thuyết phục | TV3/TV5/TV6 thống nhất bộ ảnh mẫu ngay từ đầu, TV1 duyệt trước khi thí nghiệm chính thức chạy |
| Trùng lặp/xung đột code khi tích hợp (merge conflict) | Trễ tiến độ, lỗi pipeline | Mỗi thành viên làm việc trên nhánh riêng, TV1 review trước khi merge vào `main` |

## 7. Kênh liên lạc & báo cáo tiến độ

- Mỗi thành viên báo cáo tiến độ module của mình (theo %) cho TV1 định kỳ.
- TV1 cập nhật vào `task_list.md` và tổng hợp vào `meeting_notes.md` sau mỗi buổi họp.
