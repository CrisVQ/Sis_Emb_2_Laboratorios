import cv2

# Ruta del archivo de video
video_path = 'repro.mp4'

# Cargar el video
cap = cv2.VideoCapture(video_path)

# Verificar que el video se haya cargado correctamente
if not cap.isOpened():
    print("Error al abrir el video")
    exit()

while True:
    # Leer el siguiente cuadro
    ret, frame = cap.read()
    
    # Si no hay más cuadros, salir del bucle
    if not ret:
        break

    # Redimensionar el cuadro a 400x600
    frame_resized = cv2.resize(frame, (400, 600))

    # Mostrar el cuadro redimensionado
    cv2.imshow('Video', frame_resized)

    # Salir al presionar la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
