## 2. Tại sao cần Gaussian Blur?
Bộ lọc mờ Gaussian (Gaussian Blur) được thực hiện ngay ở bước đầu tiên của thuật toán nhằm mục đích giảm nhiễu (noise reduction).  
   + Lý do kỹ thuật: Phép tính đạo hàm/gradient ở bước tiếp theo rất nhạy cảm với nhiễu. Nhờ bản chất biến đổi mức xám đột ngột, các điểm nhiễu tần số cao sẽ có giá trị gradient rất lớn, dễ bị thuật toán nhận diện nhầm thành các "cạnh giả".  
   + Cơ chế: Làm mịn ảnh bằng Kernel Gaussian 2 chiều giúp loại bỏ các biến đổi tần số cao ngẫu nhiên trước khi tìm biên:
        G(x,y) = (1 / 2πσ²) · e^(−(x²+y²)/2σ²) 
Trong đó σ (sigma) là độ lệch chuẩn, quyết định mức độ làm mịn. σ càng lớn, ảnh càng bị làm mờ nhiều, nhiễu bị loại bỏ mạnh nhưng đồng thời các chi tiết nhỏ và cạnh yếu cũng có thể bị mất. Nếu bỏ qua bước này, ảnh kết quả sau phát hiện biên sẽ chứa rất nhiều đốm nhiễu rời rạc và các đường biên giả.
## 3. Gradient Calculation
Sau khi làm mịn, ảnh được tính đạo hàm theo hai hướng x và y (thường dùng toán tử Sobel) để tìm cường độ và hướng thay đổi mức xám tại mỗi điểm ảnh:
    • Độ lớn gradient: G = √(Gx² + Gy²), thể hiện mức độ thay đổi cường độ (cạnh càng mạnh thì G càng lớn).
    • Hướng gradient: θ = atan2(Gy, Gx), thể hiện hướng vuông góc với cạnh.
Kết quả bước này là một "bản đồ cạnh thô" – các vùng có cạnh sẽ có giá trị gradient lớn, nhưng cạnh còn dày (nhiều điểm ảnh liền kề đều có gradient cao).
## 4. Non-Maximum Suppression (Triệt tiêu không cực đại)
Mục tiêu của bước này là làm mảnh cạnh, thu hẹp các dải biên dày ban đầu về đường biên có bề rộng đúng 1 pixel.  
    + Cơ chế hoạt động:Hướng gradient tại mỗi điểm ảnh được làm tròn về 1 trong 4 hướng chính: 0° (ngang), 45° (chéo phải), 90° (dọc), 135° (chéo trái).  
    + So sánh độ lớn gradient G của điểm ảnh đang xét với hai điểm ảnh lân cận nằm trên cùng hướng gradient đó.  
    + Nếu điểm ảnh đang xét có giá trị G lớn nhất (cực đại cục bộ), nó được giữ lại.  
    + Nếu không phải cực đại cục bộ, điểm ảnh đó sẽ bị triệt tiêu (gán giá trị về 0). 
## 5. Double Threshold (Ngưỡng kép)
Sau khi triệt tiêu không cực đại, ảnh vẫn còn chứa các đường biên yếu do nhiễu hoặc do biến đổi độ tương phản nhỏ. Canny sử dụng hai ngưỡng cố định: Ngưỡng cao (T_high) và Ngưỡng thấp (T_low) để phân loại các điểm ảnh thành 3 nhóm:  
    • Cạnh mạnh (strong edge): gradient ≥ ngưỡng cao → chắc chắn là cạnh thật, được giữ lại ngay.
    • Cạnh yếu (weak edge): ngưỡng thấp ≤ gradient < ngưỡng cao → có thể là cạnh thật hoặc nhiễu, cần xét tiếp ở bước 5.
    • Không phải cạnh: gradient < ngưỡng thấp → bị loại bỏ hoàn toàn.
## 6. Edge Tracking by Hysteresis (Theo dõi cạnh bằng độ trễ)
Bước này quyết định loại bỏ hay giữ lại các điểm cạnh yếu  
    + Nguyên tắc: Một điểm cạnh yếu sẽ được công nhận là cạnh thật nếu nó kề cận (liên kết theo 8 hướng lân cận) với ít nhất một điểm cạnh mạnh.  
    + Ý nghĩa:
        • Giúp khôi phục các đoạn cạnh thật bị đứt quãng do tương phản giảm cục bộ.  
        • Loại bỏ triệt để các đốm cạnh yếu cô lập (vốn sinh ra từ nhiễu còn sót lại)