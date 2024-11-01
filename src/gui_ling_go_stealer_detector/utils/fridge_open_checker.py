from typing import List,Tuple
import cv2
import numpy as np
 
def check_open(input_image:np.ndarray, threshold: List[List], bounding_area: List[List]) -> bool:
    hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)
    lower_hsv = np.array(threshold[0])
    upper_hsv = np.array(threshold[1])
    mask = cv2.inRange(hsv_image, lower_hsv, upper_hsv)
    
    x_start, y_start = bounding_area[0]
    x_end, y_end = bounding_area[1]
 
    bounding_area_mask = mask[y_start:y_end, x_start:x_end]
    total_area = bounding_area_mask.size
    masked_area = cv2.countNonZero(bounding_area_mask)
    masked_percentage = (masked_area / total_area) * 100
 
    # Check if the masked area is less than 60%
    return masked_percentage > 60
 