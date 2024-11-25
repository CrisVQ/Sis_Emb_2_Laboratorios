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
        self.camera = cv2.VideoCapture(camera)
        self.displayed = True
        self.fgbg_knn = cv2.createBackgroundSubtractorKNN()  # Inicializa el sustractor de fondo KNN

    def display_camera(self):
        self.camera_visualization()

    def stop_display(self):
        self.displayed = False
        self.camera.release()
        cv2.destroyAllWindows()

    def camera_visualization(self):
        while self.displayed:
            check, frame = self.camera.read()
            if check:
                # Aplicar la sustracción de fondo
                fgmask = self.fgbg_knn.apply(frame)

                # Encontrar los contornos de las áreas de movimiento
                contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Obtener el centro de la pantalla
                height, width, _ = frame.shape
                center_x, center_y = width // 2, height // 2

                object_detected = False
                for contour in contours:
                    if cv2.contourArea(contour) > 1000:  # Umbral para evitar detecciones pequeñas
                        x, y, w, h = cv2.boundingRect(contour)
                        if x < center_x < x + w and y < center_y < y + h:
                            object_detected = True
                            break

                # Dibujar un círculo en el centro de la pantalla (opcional)
                cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)

                # Mostrar el mensaje si se detecta un objeto
                if object_detected:
                    cv2.putText(frame, "Object Detected", (width - 250, height - 20),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Mostrar el video y la máscara
                cv2.imshow("Camera", frame)
                cv2.imshow("Foreground Mask", fgmask)
            else:
                print("Error al capturar el frame.")

            key = cv2.waitKey(1)
            if key == 27:  # 27 es el código ASCII para la tecla 'Esc'
                self.stop_display()

if __name__ == "__main__":
    camera = "http://172.18.9.117:4747/video"  # Puedes usar 0 para la webcam local
    camera_object = VideoCapture(camera)
    camera_object.display_camera()
