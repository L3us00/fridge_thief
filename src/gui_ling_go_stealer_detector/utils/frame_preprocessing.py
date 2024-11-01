import cv2
import numpy as np

def crop_right_half_image(image: np.ndarray) -> np.ndarray:
    height, width, _ = image.shape
    crop_start_x = width // 2
    crop_end_x = width
    crop_y_start = 0
    crop_y_end = height
    return image[crop_y_start:crop_y_end, crop_start_x:crop_end_x]