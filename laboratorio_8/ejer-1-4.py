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

    # Obtener las dimensiones del cuadro
    height, width = frame.shape[:2]
    
    # Dividir el cuadro en dos mitades
    left_half = frame[:, :width // 2]  # Mitad izquierda
    right_half = frame[:, width // 2:]  # Mitad derecha

    # Mostrar ambas mitades en ventanas separadas
    cv2.imshow('Left Half', left_half)
    cv2.imshow('Right Half', right_half)

    # Salir al presionar la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
