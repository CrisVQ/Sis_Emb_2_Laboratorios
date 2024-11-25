import cv2
import numpy as np
import serial

def get_color_name(b, g, r):
    if r > 200 and g < 100 and b < 100:
        return "Rojo"
    elif g > 200 and r < 100 and b < 100:
        return "Verde"
    elif b > 200 and r < 100 and g < 100:
        return "Azul"
    elif r > 200 and g > 200 and b < 100:
        return "Amarillo"
    elif r > 200 and g < 100 and b > 200:
        return "Magenta"
    elif r < 100 and g > 200 and b > 200:
        return "Cian"
    else:
        return "Color Desconocido"

image = cv2.imread('figuras.png')
if image is None:
    print("Error: No se pudo cargar la imagen. Verifica la ruta.")
    exit()

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(image_gray, 240, 255, cv2.THRESH_BINARY_INV)
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(approx)
    if len(approx) == 3:
        shape = "Triangulo"
    elif len(approx) == 4:
        aspect_ratio = w / float(h)
        shape = "Cuadrado" if 0.95 <= aspect_ratio <= 1.05 else "Rectangulo"
    elif len(approx) > 4:
        shape = "Circulo"
    else:
        shape = "Indefinido"

    mask = np.zeros(image_gray.shape, np.uint8)
    cv2.drawContours(mask, [contour], -1, 255, -1)
    mean_color = cv2.mean(image, mask=mask)[:3]
    color_name = get_color_name(int(mean_color[0]), int(mean_color[1]), int(mean_color[2]))

    cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.putText(image, color_name, (x, y + h + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

object_count = len(contours)
if object_count > 1:
    ser = serial.Serial('COMx', 9600)  # Cambia 'COMx' al puerto adecuado
    ser.write(b'1')  # Enciende todos los LEDs
else:
    ser = serial.Serial('COMx', 9600)
    ser.write(b'2')  # Enciende 2 LEDs

cv2.imshow("Figuras Detectadas", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
