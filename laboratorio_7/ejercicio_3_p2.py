import cv2
import numpy as np

class ImageColorConverter:
    def __init__(self, img_path):
        self.img = cv2.imread(img_path)
        if self.img is None:
            raise ValueError("No se pudo cargar la imagen.")

    def to_rgb(self):
        # Verificar si ya está en RGB, ya que OpenCV lee imágenes en formato BGR por defecto
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)

    def to_hsv(self):
        # Convertir la imagen de BGR a HSV
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    def to_grayscale(self):
        # Convertir la imagen a escala de grises
        return cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def show_image(self, img, title):
        # Mostrar la imagen con el título dado
        cv2.imshow(title, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Ruta de la imagen
    img_path = "colors/blue.jpg"
    
    # Crear instancia de la clase
    converter = ImageColorConverter(img_path)
    
    # Convertir y mostrar la imagen en diferentes espacios de color
    rgb_img = converter.to_rgb()
    hsv_img = converter.to_hsv()
    grayscale_img = converter.to_grayscale()

    # Mostrar las imágenes modificadas
    converter.show_image(rgb_img, "Imagen en RGB")
    converter.show_image(hsv_img, "Imagen en HSV")
    converter.show_image(grayscale_img, "Imagen en escala de grises")
