import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('face_detector.xml')

# Read the input image
img = cv2.imread('image.jpg')

# Convert to grayscale (recommended for Haar detection)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Save the result image
cv2.imwrite('face_detected.png', img)
print("Successfully saved face_detected.png")
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
