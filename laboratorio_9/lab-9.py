import cv2
import numpy as np

# Cargar una imagen
img = cv2.imread('imagen.jpg')

# Verificar si la imagen se ha cargado correctamente
if img is None:
    print("Error: No se pudo cargar la imagen.")
else:
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)
    mblur = cv2.medianBlur(img, kernel)

    # Mostrar la imagen original y la imagen filtrada
    cv2.imshow('Imagen Original', img)
    cv2.imshow('Imagen Filtrada', dst)
    cv2.imshow('Imagen m-blur', mblur)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
