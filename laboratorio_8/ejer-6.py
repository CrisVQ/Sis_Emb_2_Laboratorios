import cv2
#import numpy as np

class ContourDetector:
    def __init__(self):
        self.camera = "http://192.168.31.47:4747/video"
        self.cap = cv2.VideoCapture(self.camera)  # Abre la cámara

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Apply Gaussian blur to reduce noise
            blurred = cv2.GaussianBlur(gray, (5, 5), 0)

            # Perform Canny edge detection
            edges = cv2.Canny(blurred, 50, 150)

            # Find contours
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Draw contours on the original frame
            cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)  # Green color, thickness 2

            # Display the resulting frame
            cv2.imshow("Contour Detection", frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close all OpenCV windows
        self.cap.release()
        cv2.destroyAllWindows()

# Run the contour detector application
if __name__ == "__main__":
    detector = ContourDetector()
    detector.run()
