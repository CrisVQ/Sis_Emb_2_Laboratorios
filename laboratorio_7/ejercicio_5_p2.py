import cv2
from abc import ABC, abstractmethod

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
        self.camera = cv2.VideoCapture(camera)  # Inicializa el objeto VideoCapture
        self.displayed = False
        self.display_mode = 'rgb'  # Modo inicial de visualización

    def display_camera(self):
        self.displayed = True
        self.camera_visualization()

    def stop_display(self):
        self.displayed = False
        self.camera.release()  # Libera la cámara
        cv2.destroyAllWindows()  # Cierra todas las ventanas de OpenCV

    def camera_visualization(self):
        while self.displayed:
            check, frame = self.camera.read()
            if check:
                # Muestra el frame en función del modo de visualización actual
                if self.display_mode == 'grayscale':
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("camera", gray_frame)
                else:
                    cv2.imshow("camera", frame)
            else:
                print("Error al capturar el frame.")

            key = cv2.waitKey(1) & 0xFF  # Lee una tecla
            if key == ord('g'):  # Cambia a escala de grises
                self.display_mode = 'grayscale'
            elif key == ord('r'):  # Cambia a RGB
                self.display_mode = 'rgb'
            elif key == 27:  # 27 es el código ASCII para la tecla 'Esc'
                self.stop_display()

if __name__ == "__main__":
    camera = "http://192.168.31.47:4747/video"
    camera_object = VideoCapture(camera)
    camera_object.display_camera()
