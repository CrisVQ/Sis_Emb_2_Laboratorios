import cv2

# Cargar la imagen
imagen = cv2.imread('img.jpg')

# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización
_, imagen_binaria = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY)

# Encontrar contornos
contornos, jerarquia = cv2.findContours(imagen_binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar contornos en la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)  # Dibuja todos los contornos en verde

# Mostrar la imagen original con contornos
cv2.imshow('Contornos', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
