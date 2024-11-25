import cv2


def resize_img(img, width, height):
    up_points = (width, height)
    img_resize = cv2.resize(img, up_points)
    return img_resize

if __name__ == "__main__":
    img = cv2.imread("imagen.jpg")

    original_height, original_width = img.shape[:2]

    # Mostrar opciones al usuario
    print("Selecciona un tamaño:")
    print("1. Tamaño original")
    print("2. Pequeño (25% del original)")
    print("3. Mediano (50% del original)")
    print("4. Grande (75% del original)")
        
    # Leer la elección del usuario
    choice = input("Introduce el número de tu elección: ")

    # Aplicar redimensionado según la selección
    if choice == '1':
        resized_img = img  # Mantener el tamaño original
    elif choice == '2':
        resized_img = resize_img(img, original_width // 4, original_height // 4)  # 25%
    elif choice == '3':
        resized_img = resize_img(img, original_width // 2, original_height // 2)  # 50%
    elif choice == '4':
        resized_img = resize_img(img, int(original_width * 0.75), int(original_height * 0.75))  # 75%    
    
    

    # Mostrar la imagen redimensionada
    cv2.imshow("Imagen Redimensionada", resized_img)

    cv2.waitKey(0)