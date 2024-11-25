import cv2

def show_image(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)

def resize_image(img, width, height):
    resized_img = cv2.resize(img, (width, height))
    return resized_img

def cut_image_horizontally(img):
    height, width, _ = img.shape
    half_height = height // 2
    top_half = img[:half_height, :]
    bottom_half = img[half_height:, :]
    return top_half, bottom_half

def cut_image_vertically(img):
    height, width, _ = img.shape
    half_width = width // 2
    left_half = img[:, :half_width]
    right_half = img[:, half_width:]
    return left_half, right_half

def divide_image_quadrants(img):
    height, width, _ = img.shape
    half_height = height // 2
    half_width = width // 2
    quadrant_1 = img[:half_height, :half_width]  # Top-left
    quadrant_2 = img[:half_height, half_width:]  # Top-right
    quadrant_3 = img[half_height:, :half_width]  # Bottom-left
    quadrant_4 = img[half_height:, half_width:]  # Bottom-right
    return quadrant_1, quadrant_2, quadrant_3, quadrant_4

if __name__ == "__main__":
    img = cv2.imread("imagen.jpg")

    # Show original image
    #show_image("Original Image", img)

    # Resize the image to 400x600 (width, height)
    resized_img = resize_image(img, 400, 600)
    show_image("Resized Image (400x600)", resized_img)

    # Cut the image horizontally
    top_half, bottom_half = cut_image_horizontally(resized_img)
    show_image("Top Half", top_half)
    show_image("Bottom Half", bottom_half)

    # Cut the image vertically
    left_half, right_half = cut_image_vertically(resized_img)
    show_image("Left Half", left_half)
    show_image("Right Half", right_half)

    # Divide the image into quadrants
    quadrant_1, quadrant_2, quadrant_3, quadrant_4 = divide_image_quadrants(resized_img)
    show_image("Quadrant 1", quadrant_1)
    show_image("Quadrant 2", quadrant_2)
    show_image("Quadrant 3", quadrant_3)
    show_image("Quadrant 4", quadrant_4)

    cv2.destroyAllWindows()
