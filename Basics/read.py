import cv2 as cv

## TO READ AN IMAGE
img = cv.imread('C:/Users/Akash Ray/Desktop/fish_large.jpg')

cv.imshow("Fish",img)


## TO READ A VIDEO
# reads the video from specified path
# capture = cv.VideoCapture('OpenCV Project/Coffee & Donut.mp4')

# reads the video from webcam
capture = cv.VideoCapture(1, cv.CAP_DSHOW)

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    # Stops execution when pressed 'd'
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
