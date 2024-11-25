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
        # Crea el objeto de sustracción de fondo KNN
        self.bg_subtractor = cv2.createBackgroundSubtractorKNN()

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
                # Aplica la sustracción de fondo
                fg_mask = self.bg_subtractor.apply(frame)

                # Obtiene las dimensiones del frame
                height, width = frame.shape[:2]

                # Define una región central (un área de detección)
                center_x1 = width // 2 - 50
                center_x2 = width // 2 + 50
                center_y1 = height // 2 - 50
                center_y2 = height // 2 + 50

                # Extrae la región central de la máscara de primer plano
                center_region = fg_mask[center_y1:center_y2, center_x1:center_x2]

                # Contar los píxeles blancos en la región central
                white_pixels = cv2.countNonZero(center_region)

                # Si se detectan más de 50 píxeles blancos, se considera un objeto detectado
                if white_pixels > 50:
                    cv2.putText(frame, "Objeto detectado", (width - 200, height - 20), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

                # Dibuja un rectángulo en la región central para referencia visual
                cv2.rectangle(frame, (center_x1, center_y1), (center_x2, center_y2), (0, 255, 0), 2)

                # Muestra el frame original y la máscara de primer plano
                cv2.imshow("Original Camera Feed", frame)
                cv2.imshow("Foreground Mask", fg_mask)
            else:
                print("Error al capturar el frame.")

            key = cv2.waitKey(1)
            if key == 27:  # 27 es el código ASCII para la tecla 'Esc'
                self.stop_display()

if __name__ == "__main__":
    camera = "http://172.18.9.117:4747/video" 
    camera_object = VideoCapture(camera)
    camera_object.display_camera()
