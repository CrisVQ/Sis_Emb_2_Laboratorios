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
    
    # Calcular los puntos medios
    mid_height = height // 2
    mid_width = width // 2

    # Dividir el cuadro en cuatro cuadrantes
    top_left = frame[:mid_height, :mid_width]        # Cuadrante superior izquierdo
    top_right = frame[:mid_height, mid_width:]       # Cuadrante superior derecho
    bottom_left = frame[mid_height:, :mid_width]     # Cuadrante inferior izquierdo
    bottom_right = frame[mid_height:, mid_width:]    # Cuadrante inferior derecho

    # Mostrar cada cuadrante en una ventana separada
    cv2.imshow('Top Left', top_left)
    cv2.imshow('Top Right', top_right)
    cv2.imshow('Bottom Left', bottom_left)
    cv2.imshow('Bottom Right', bottom_right)

    # Salir al presionar la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
