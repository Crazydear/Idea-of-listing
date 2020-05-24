import cv2
import sys

'''# Get user supplied values
cap = cv2.VideoCapture(0)
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
ret,image = cap.read()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)
print("Found {0} faces!".format(len(faces)))
# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces found", image)
cv2.waitKey(0)'''

def face_detect_demo(image):
    cascPath = "haarcascade_frontalface_default.xml"
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_detector = cv2.CascadeClassifier(cascPath)
    faces = face_detector.detectMultiScale(gray, 1.6,5)
    print(len(faces))
    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow("result", image)
print("--------- Python OpenCV Tutorial ---------")
capture = cv2.VideoCapture(0)
cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
while (True):
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)
    face_detect_demo(frame)
    c = cv2.waitKey(10)
    if c == 27:  # ESC,q
        break

capture.release()
cv2.destroyAllWindows()
