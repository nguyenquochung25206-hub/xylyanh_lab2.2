from pathlib import Path
 
import cv2
import numpy as np
 
 
def save_result(image: np.ndarray, output_path: str) -> None:
    """
    Lưu một ảnh (numpy array) ra đường dẫn output_path.
    Tự động tạo thư mục cha nếu chưa tồn tại.
 
    Args:
        image: ảnh dạng numpy array (grayscale hoặc màu).
        output_path: đường dẫn file đích, ví dụ 'data/output/opencv/anh1.png'.
 
    Raises:
        IOError: nếu OpenCV không lưu được ảnh (sai định dạng, ảnh rỗng...).
    """
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
 
    success = cv2.imwrite(str(path), image)
    if not success:
        raise IOError(f"Không thể lưu ảnh tại: {output_path}")
 
