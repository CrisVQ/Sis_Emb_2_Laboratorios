import cv2

# Cargar el video
video = cv2.VideoCapture('bouncing.mp4')

# Crear los sustractores de fondo
fgbg_mog2 = cv2.createBackgroundSubtractorMOG2()
fgbg_knn = cv2.createBackgroundSubtractorKNN()

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # Aplicar la sustracción de fondo
    fgmask_mog2 = fgbg_mog2.apply(frame)
    fgmask_knn = fgbg_knn.apply(frame)

    # Mostrar los resultados
    cv2.imshow('Original', frame)
    cv2.imshow('MOG2 Subtraction', fgmask_mog2)
    cv2.imshow('KNN Subtraction', fgmask_knn)

    # Salir al presionar 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar los recursos
video.release()
cv2.destroyAllWindows()
