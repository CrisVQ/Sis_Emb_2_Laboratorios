import cv2

# Crear el objeto para la sustracción de fondo
fgbg = cv2.createBackgroundSubtractorMOG2()

# Abrir el video (0 para webcam o el nombre de archivo para un video guardado)
#cap = cv2.VideoCapture("http://192.168.31.47:4747/video")
cap = cv2.VideoCapture('bouncing.mp4')
# Verificar si se abrió correctamente
if not cap.isOpened():
    print("Error: No se pudo abrir el video.")
    exit()

while True:
    ret, frame = cap.read()  # Leer cada cuadro del video
    if not ret:
        break

    # Aplicar la sustracción de fondo
    fgmask = fgbg.apply(frame)

    # Mostrar el cuadro original y el cuadro con el fondo sustraído
    cv2.imshow('Frame', frame)
    cv2.imshow('Foreground Mask', fgmask)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
