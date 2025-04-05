# image_geometry_exercise.py
# STUDENT'S EXERCISE FILE

"""
Exercise:
Implement a function `apply_geometric_transformations(img)` that receives a grayscale image
represented as a NumPy array (2D array) and returns a dictionary with the following transformations:

1. Translated image (shift right and down)
2. Rotated image (90 degrees clockwise)
3. Horizontally stretched image (scale width by 1.5)
4. Horizontally mirrored image (flip along vertical axis)
5. Barrel distorted image (simple distortion using a radial function)

You must use only NumPy to implement these transformations. Do NOT use OpenCV, PIL, skimage or similar libraries.

Function signature:
    def apply_geometric_transformations(img: np.ndarray) -> dict:

The return value should be like:
{
    "translated": np.ndarray,
    "rotated": np.ndarray,
    "stretched": np.ndarray,
    "mirrored": np.ndarray,
    "distorted": np.ndarray
}
"""

import numpy as np

def apply_geometric_transformations(img: np.ndarray) -> dict:
    
    h, w = img.shape

    translated = np.zeros_like(img)
    dy, dx = 20, 20
    translated[dy:h, dx:w] = img[0:h-dy, 0:w-dx]

    rotated = np.rot90(img, 3)

    new_w = int(w * 1.5)
    stretched = np.zeros((h, new_w))
    for i in range(new_w):
        new_x = int(i / 1.5)
        if new_x < w:
            stretched[:, i] = img[:, new_x]

    mirrored = np.flip(img, axis=1)

    distorted = np.zeros_like(img)
    cx, cy = w // 2, h // 2
    k = 0.0005  
    for y in range(h):
        for x in range(w):
            dx = (x - cx) / w
            dy = (y - cy) / h
            r2 = dx**2 + dy**2
            factor = 1 + k * r2
            new_x = int(cx + dx * w * factor)
            new_y = int(cy + dy * h * factor)
            if 0 <= new_x < w and 0 <= new_y < h:
                distorted[y, x] = img[new_y, new_x]

    return {
        "translated": translated,
        "rotated": rotated,
        "stretched": stretched,
        "mirrored": mirrored,
        "distorted": distorted
    }
    pass