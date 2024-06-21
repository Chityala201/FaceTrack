import cv2

# Load the pre-trained face detection model
f_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the video capture device
capture = cv2.VideoCapture(0)

# Check if the video capture device is opened successfully
if not capture.isOpened():
    print("Error: Could not open video capture device.")
    exit()

while True:
    # Read a frame from the video capture device
    ret, img = capture.read()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Convert the captured frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    face = f_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw rectangles around detected faces
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the frame with detected faces
    cv2.imshow('img', img)

    # Wait for 30ms and check if the 'Esc' key is pressed
    d = cv2.waitKey(30) & 0xff
    if d == 27:  # ASCII code for 'Esc' key
        break

# Release the video capture device and close all OpenCV windows
capture.release()
cv2.destroyAllWindows()
