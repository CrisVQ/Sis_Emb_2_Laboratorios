import cv2
import os

class WebcamCapture:
    def __init__(self):
        self.camera = "http://192.168.31.47:4747/video"
        self.cap = cv2.VideoCapture(self.camera)  # Abre la cámara
        self.image_count = 1  # Contador para las imágenes capturadas
        self.captures_dir = "Captures"
        
        # Crea la carpeta 'Captures' si no existe
        if not os.path.exists(self.captures_dir):
            os.makedirs(self.captures_dir)

        # Verifica si se pudo abrir la cámara
        if not self.cap.isOpened():
            print("Error: No se puede abrir la cámara.")
            exit()

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            # Guarda la imagen con el formato "Captures/image#.jpg"
            image_path = os.path.join(self.captures_dir, f"image{self.image_count}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Imagen guardada en {image_path}")
            self.image_count += 1
            return frame
        return None

    def process_image(self, image_path):
        # Lee la imagen y la convierte a escala de grises
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if image is None:
            print("Error: La imagen no se pudo leer.")
            return

        # Divide la imagen en cuatro cuadrantes
        height, width = image.shape
        half_height, half_width = height // 2, width // 2
        
        quadrants = {
            "Top-Left": image[:half_height, :half_width],
            "Top-Right": image[:half_height, half_width:],
            "Bottom-Left": image[half_height:, :half_width],
            "Bottom-Right": image[half_height:, half_width:]
        }
        
        # Muestra cada cuadrante en una ventana
        for name, quadrant in quadrants.items():
            cv2.imshow(name, quadrant)

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                cv2.imshow("Webcam", frame)
                # Captura una imagen al presionar 'c'
                key = cv2.waitKey(1) & 0xFF
                if key == ord('c'):
                    self.capture_image()
                elif key == ord('q'):
                    break

        # Procesa la última imagen capturada
        if self.image_count > 1:
            last_image_path = os.path.join(self.captures_dir, f"image{self.image_count - 1}.jpg")
            self.process_image(last_image_path)

        # Libera la cámara y cierra ventanas
        self.cap.release()
        cv2.destroyAllWindows()

# Ejecuta la aplicación
if __name__ == "__main__":
    app = WebcamCapture()
    app.run()
