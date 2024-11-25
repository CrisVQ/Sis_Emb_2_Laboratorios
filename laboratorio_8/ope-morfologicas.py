import cv2
import numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar un umbral para obtener una imagen binaria
_, imagen_binaria = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)

# Definir un elemento estructurante
kernel = np.ones((5, 5), np.uint8)

# Erosión
imagen_erosion = cv2.erode(imagen_binaria, kernel, iterations=1)

# Dilatación
imagen_dilatacion = cv2.dilate(imagen_binaria, kernel, iterations=1)

# Apertura
imagen_apertura = cv2.morphologyEx(imagen_binaria, cv2.MORPH_OPEN, kernel)

# Cierre
imagen_cierre = cv2.morphologyEx(imagen_binaria, cv2.MORPH_CLOSE, kernel)

# Mostrar los resultados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Binaria', imagen_binaria)
cv2.imshow('Erosión', imagen_erosion)
cv2.imshow('Dilatación', imagen_dilatacion)
cv2.imshow('Apertura', imagen_apertura)
cv2.imshow('Cierre', imagen_cierre)

cv2.waitKey(0)
cv2.destroyAllWindows()
