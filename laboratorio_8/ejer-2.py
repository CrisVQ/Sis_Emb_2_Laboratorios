import cv2

class CameraFilterApp:
    def __init__(self):
        self.camera = "http://192.168.31.47:4747/video"
        self.cap = cv2.VideoCapture(self.camera)  # Abre la cámara
        self.filter = "normal"  # Filtro inicial

    def apply_filter(self, frame):
        if self.filter == "grayscale":
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif self.filter == "blur":
            return cv2.GaussianBlur(frame, (15, 15), 0)
        elif self.filter == "edges":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.Canny(gray, 50, 150)
        return frame

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Aplicar el filtro seleccionado
            filtered_frame = self.apply_filter(frame)

            # Muestra el resultado
            cv2.imshow("Camera with Filters", filtered_frame)

            # Captura teclas para seleccionar filtros
            key = cv2.waitKey(1) & 0xFF
            if key == ord('1'):
                self.filter = "normal"
            elif key == ord('2'):
                self.filter = "grayscale"
            elif key == ord('3'):
                self.filter = "blur"
            elif key == ord('4'):
                self.filter = "edges"
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Ejecuta la aplicación
if __name__ == "__main__":
    app = CameraFilterApp()
    app.run()
