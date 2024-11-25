import cv2
from abc import ABC, abstractmethod
import os

class video_capture_abs(ABC):
    @abstractmethod
    def display_camera(self):
        pass
    
    @abstractmethod
    def stop_display(self):
        pass
    
    @abstractmethod
    def camera_visualization(self):
        pass

class VideoCapture(video_capture_abs):
    def __init__(self, camera) -> None:
        self.camera = cv2.VideoCapture(camera)
        self.displayed = False
        self.display_mode = 'rgb'
        self.capture_count = 0
        self.last_capture_path = None
        os.makedirs("Captures", exist_ok=True)

    def display_camera(self):
        self.displayed = True
        self.camera_visualization()

    def stop_display(self):
        self.displayed = False
        self.camera.release()
        cv2.destroyAllWindows()
        if self.last_capture_path:
            self.process_last_capture()

    def camera_visualization(self):
        while self.displayed:
            check, frame = self.camera.read()
            if check:
                if self.display_mode == 'grayscale':
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("camera", gray_frame)
                else:
                    cv2.imshow("camera", frame)
            else:
                print("Error al capturar el frame.")

            key = cv2.waitKey(1) & 0xFF
            if key == ord('g'):
                self.display_mode = 'grayscale'
            elif key == ord('r'):
                self.display_mode = 'rgb'
            elif key == ord('c'):
                self.capture_count += 1
                file_path = f"Captures/image{self.capture_count}.jpg"
                cv2.imwrite(file_path, frame)
                self.last_capture_path = file_path
                print(f"Imagen capturada y guardada en {file_path}")
            elif key == 27:
                self.stop_display()

    def process_last_capture(self):
        image = cv2.imread(self.last_capture_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            print("No se encontró la última imagen capturada.")
            return
        
        h, w = image.shape
        half_h, half_w = h // 2, w // 2

        quadrants = [
            ("Quadrant 1", image[0:half_h, 0:half_w]),
            ("Quadrant 2", image[0:half_h, half_w:w]),
            ("Quadrant 3", image[half_h:h, 0:half_w]),
            ("Quadrant 4", image[half_h:h, half_w:w]),
        ]

        for name, quadrant in quadrants:
            cv2.imshow(name, quadrant)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera = "http://192.168.31.47:4747/video"
    camera_object = VideoCapture(camera)
    camera_object.display_camera()
