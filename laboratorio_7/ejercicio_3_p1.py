import cv2

def rotate_image(img):
    # Rota la imagen 90 grados en sentido horario
    return cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

if __name__ == "__main__":
    # Cargar la imagen desde un archivo
    img = cv2.imread("imagen.jpg")

    # Verificar si la imagen fue cargada correctamente
    if img is None:
        print("Error: No se pudo cargar la imagen.")
    else:
        # Mostrar la imagen original
        #cv2.imshow("Imagen Original", img)
        
        while True:
            # Esperar a que el usuario presione una tecla
            key = cv2.waitKey(0)  # Espera indefinidamente hasta que se presione una tecla
            
            # Rotar la imagen
            img = rotate_image(img)
            
            # Mostrar la imagen rotada
            cv2.imshow("Imagen Rotada", img)
            
            # Salir del bucle si se presiona la tecla 'q'
            if key == ord('q'):
                break

        cv2.destroyAllWindows()
