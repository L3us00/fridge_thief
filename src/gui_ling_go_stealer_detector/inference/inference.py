import cv2
from src.gui_ling_go_stealer_detector.config.config import Config
from src.gui_ling_go_stealer_detector.utils.fridge_open_checker import check_open
from src.gui_ling_go_stealer_detector.utils.frame_preprocessing import crop_right_half_image

class Inference:
    def __init__(self):
        self.config = Config()
        self.cap = cv2.VideoCapture(0)

    def run_cam(self):
        if not self.cap.isOpened():
            print("Error: Could not open webcam.")
        else:
            while True:
                ret, frame = self.cap.read()
                frame = crop_right_half_image(frame)
                print(check_open(frame, self.config.threshold, self.config.bounding_area))
                if not ret:
                    print("Error: Could not read frame.")
                    break
                cv2.imshow('Webcam', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
        self.cap.release()
        cv2.destroyAllWindows()