import cv2
import numpy as np

def resize_img(img, width, height):
    up_points = (width, height)
    img_resize = cv2.resize(img, up_points)
    return img_resize

def detect_color(img):
    # Calculamos la media de los valores de los canales de color
    mean_bgr = np.mean(img, axis=(0, 1))
    # El color predominante será el canal que tenga mayor media
    colors = ['Blue', 'Green', 'Red']
    dominant_color = colors[np.argmax(mean_bgr)]
    return dominant_color

if __name__ == "__main__":
    img = cv2.imread("colors/blue.jpg")
    if img is None:
        print("No se pudo cargar la imagen.")
    else:
        dominant_color = detect_color(img)
        print(f"El color predominante es: {dominant_color}")
    
    # Mostramos la imagen
    cv2.imshow("Imagen original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
