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

    # Convertir el cuadro a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Aplicar el detector de bordes de Canny
    edges = cv2.Canny(gray_frame, 100, 200)

    # Mostrar el cuadro con bordes detectados
    cv2.imshow('Edge Detector', edges)

    # Salir al presionar la tecla 'q'
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar ventanas
cap.release()
cv2.destroyAllWindows()
