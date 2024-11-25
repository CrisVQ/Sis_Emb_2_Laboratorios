import cv2
import numpy as np

# Load the image
image = cv2.imread('monedas_2.jpg')
if image is None:
    raise Exception("Error loading image. Make sure 'monedas_2.jpg' exists in your directory.")

# Resize the image to half its original size
image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Use adaptive thresholding to create a binary image
thresholded = cv2.adaptiveThreshold(
    blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2
)

# Apply morphological operations to close gaps in the coins' contours
kernel = np.ones((3, 3), np.uint8)
morph = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel, iterations=2)

# Find contours in the processed image
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours and count them
for contour in contours:
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Display the result
print(f"Number of coins detected: {len(contours)}")

cv2.imshow("Coins Detected", image)
cv2.imshow("Processed Image", morph)
cv2.waitKey(0)
cv2.destroyAllWindows()
