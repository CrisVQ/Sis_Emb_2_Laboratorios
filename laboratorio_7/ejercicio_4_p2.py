import cv2
import numpy as np

class ImageColorConverter:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path)
        if self.img is None:
            raise ValueError("No se pudo cargar la imagen.")

    def to_hsv(self):
        # Convertir la imagen de BGR a HSV
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def detect_color_hsv(self, hsv_img):
        # Definimos los rangos para diferentes colores en HSV
        # Los valores del canal de matiz (H) son entre 0 y 179, Saturación (S) y Valor (V) entre 0 y 255.
        
        # Definición de los rangos para diferentes colores
        colors_ranges = {
            "Red": [(0, 50, 50), (10, 255, 255)],  # Rango para el color rojo
            "Green": [(35, 50, 50), (85, 255, 255)],  # Rango para el color verde
            "Blue": [(100, 50, 50), (140, 255, 255)]  # Rango para el color azul
        }

        detected_colors = []

        for color_name, (lower, upper) in colors_ranges.items():
            lower_bound = np.array(lower, dtype=np.uint8)
            upper_bound = np.array(upper, dtype=np.uint8)

            # Crear una máscara que incluya solo los píxeles dentro del rango de colores
            mask = cv2.inRange(hsv_img, lower_bound, upper_bound)

            # Si hay píxeles dentro del rango, añadimos el color detectado a la lista
            if cv2.countNonZero(mask) > 0:
                detected_colors.append(color_name)

        return detected_colors

    def show_image(self, img, title):
        # Mostrar la imagen con el título dado
        cv2.imshow(title, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ruta de la imagen
    img_path = "colors/red.jpg"
    
    # Crear instancia de la clase
    converter = ImageColorConverter(img_path)
    
    # Convertir la imagen a HSV
    hsv_img = converter.to_hsv()

    # Detectar colores en la imagen usando HSV
    detected_colors = converter.detect_color_hsv(hsv_img)
    
    # Imprimir los colores detectados
    if detected_colors:
        print(f"Colores detectados: {', '.join(detected_colors)}")
    else:
        print("No se detectaron colores.")
    
    # Mostrar la imagen original
    converter.show_image(converter.img, "Imagen original")
