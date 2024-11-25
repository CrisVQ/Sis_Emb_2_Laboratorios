import cv2

# Cargar la imagen en escala de grises
image = cv2.imread('bouncing.mp4', cv2.IMREAD_GRAYSCALE)

# Aplicar binarización adaptativa
adaptive_image = cv2.adaptiveThreshold(
    image,
    255,                        # Valor máximo para los píxeles binarizados
    cv2.ADAPTIVE_THRESH_MEAN_C, # Método de binarización adaptativa
    cv2.THRESH_BINARY,          # Tipo de binarización
    11,                         # Tamaño de la vecindad (un valor impar)
    2                           # Constante que se resta al promedio local
)

# Mostrar la imagen binarizada
cv2.imshow('Adaptive Threshold', adaptive_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
