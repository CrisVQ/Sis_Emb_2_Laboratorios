import cv2

# Cargar la imagen
imagen = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar thresholding
umbral = 128  # Valor de umbral
_, imagen_binaria = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)

# Mostrar la imagen original y la imagen binaria
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Binaria', imagen_binaria)
cv2.waitKey(0)
cv2.destroyAllWindows()
