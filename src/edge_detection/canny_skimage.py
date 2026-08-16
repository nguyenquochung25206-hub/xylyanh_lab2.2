
import numpy as np
from skimage import color, feature
from skimage.util import img_as_float, img_as_ubyte


def canny_skimage(
    image,
    sigma=1.0,
    low_threshold=None,
    high_threshold=None,
    use_quantiles=False,
    mask=None,
    mode="constant",
    cval=0.0,
):
    """
    Apply Canny edge detection using scikit-image.

    Parameters
    ----------
    image : numpy.ndarray
        Input image (RGB or grayscale).
    sigma : float, optional
        Standard deviation of the Gaussian filter.
    low_threshold : float, optional
        Lower threshold for hysteresis. If None, auto-computed.
    high_threshold : float, optional
        Upper threshold for hysteresis. If None, auto-computed.
    use_quantiles : bool, optional
        If True, treat low/high_threshold as quantiles (0-1).
    mask : numpy.ndarray, optional
        Binary mask to restrict edge detection.
    mode : str, optional
        Padding mode (see skimage documentation).
    cval : float, optional
        Constant value for padding (if mode='constant').

    Returns
    -------
    edges : numpy.ndarray (uint8)
        Binary edge image with values 0 and 255.
    """
    # Convert to grayscale if needed
    if image.ndim == 3 and image.shape[-1] == 3:
        gray = color.rgb2gray(image)
    elif image.ndim == 3 and image.shape[-1] == 4:
        # RGBA – take only RGB channels
        gray = color.rgb2gray(image[:, :, :3])
    else:
        gray = image.copy()
        # If still multi-channel (e.g., 2D+), force 2D
        if gray.ndim > 2:
            gray = gray[:, :, 0]

    # Ensure float in [0, 1]
    if gray.dtype not in (np.float32, np.float64):
        gray = img_as_float(gray)

    # Apply Canny
    edges_bool = feature.canny(
        gray,
        sigma=sigma,
        low_threshold=low_threshold,
        high_threshold=high_threshold,
        mask=mask,
        use_quantiles=use_quantiles,
        mode=mode,
        cval=cval,
    )

    # Convert boolean mask to uint8 (0 and 255)
    return img_as_ubyte(edges_bool)
