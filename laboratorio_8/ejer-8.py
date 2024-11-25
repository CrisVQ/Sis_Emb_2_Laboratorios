import cv2

class CameraFilterApp:
    def __init__(self):
        self.camera = "http://192.168.31.47:4747/video"
        self.cap = cv2.VideoCapture(self.camera)  # Abre la cámara
        self.filter = "normal"  # Filtro inicial
        # Crea el sustractor de fondo
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()

    def apply_filter(self, frame):
        if self.filter == "grayscale":
            return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        elif self.filter == "blur":
            return cv2.GaussianBlur(frame, (15, 15), 0)
        elif self.filter == "edges":
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return cv2.Canny(gray, 50, 150)
        elif self.filter == "background_subtraction":
            # Aplica la sustracción de fondo
            fg_mask = self.background_subtractor.apply(frame)
            return fg_mask
        return frame

    def detect_movement(self, fg_mask):
        # Calcula el área del primer plano (movimiento)
        movement_area = cv2.countNonZero(fg_mask)
        # Umbral para detectar movimiento (ajústalo según sea necesario)
        threshold = 50000
        if movement_area > threshold:
            return True
        return False

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Aplicar el filtro seleccionado
            filtered_frame = self.apply_filter(frame)

            # Si el filtro es sustracción de fondo, detecta movimiento
            if self.filter == "background_subtraction":
                movement_detected = self.detect_movement(filtered_frame)
                if movement_detected:
                    cv2.putText(frame, "Movimiento detectado!", (10, 30), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Muestra el resultado
            cv2.imshow("Camera with Filters", frame if self.filter == "background_subtraction" else filtered_frame)

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
            elif key == ord('5'):
                self.filter = "background_subtraction"  # Nuevo filtro
            elif key == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

# Ejecuta la aplicación
if __name__ == "__main__":
    app = CameraFilterApp()
    app.run()
