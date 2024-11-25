import cv2

def resize_img(img, width, height):
    up_points = (width, height)
    img_resize = cv2.resize(img, up_points)
    return img_resize

if __name__ == "__main__":
    img = cv2.imread("imagen.jpg")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises
    rimg = resize_img(gray_img, 1000, 1000)
    cv2.imshow("resize grayscale image", rimg)
    cv2.waitKey(0)
