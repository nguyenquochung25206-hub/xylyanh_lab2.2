### 10. Cơ sở lý thuyết về tham số 
### Sigma σ trong Gaussian Filter

| Thay đổi tham số | Ảnh hưởng đến kết quả |
| :----- | :--- |
| σ tăng | Ảnh bị làm mờ nhiều hơn → loại bỏ nhiễu tốt hơn, nhưng có thể làm mất các cạnh nhỏ/yếu và làm cạnh bị dịch chuyển nhẹ vị trí; số lượng cạnh phát hiện được giảm. |
| σ giảm | Ảnh giữ được nhiều chi tiết hơn, cạnh sắc nét hơn, nhưng nhiễu không được lọc hết → dễ sinh ra nhiều cạnh giả do nhiễu. |

---

### Ngưỡng thấp và ngưỡng cao (Low / High Threshold)

| Thay đổi tham số       | Ảnh hưởng đến kết quả |
| :--------------------- | :-------------------- |
| Ngưỡng thấp (low) tăng | Nhiều cạnh yếu bị loại bỏ ngay từ bước ngưỡng kép → cạnh bị đứt quãng nhiều hơn, ảnh cạnh "thưa" hơn. |
| Ngưỡng thấp (low) giảm | Nhiều điểm được giữ lại làm cạnh yếu ứng viên → cạnh liền mạch hơn nhưng dễ giữ lại cả nhiễu nếu nó liên kết với cạnh mạnh. |
| Ngưỡng cao (high) tăng | Chỉ những cạnh có độ tương phản rất mạnh mới được công nhận là "cạnh mạnh" ngay → tổng số cạnh phát hiện giảm, có thể bỏ sót cạnh thật. |
| Ngưỡng cao (high) giảm | Nhiều điểm được công nhận là cạnh mạnh hơn → phát hiện được nhiều cạnh hơn, nhưng tăng nguy cơ nhận nhiễu thành cạnh mạnh. |