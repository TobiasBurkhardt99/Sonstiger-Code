import cv2

# Start the webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise Exception("Could not open video device")

# Read a frame from the webcam
ret, frame = cap.read()

# Release the webcam
cap.release()

# Display the captured image
cv2.imshow('Captured Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
