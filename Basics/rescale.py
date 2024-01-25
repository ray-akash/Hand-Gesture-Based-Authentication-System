import cv2 as cv

def rescaleFrame(frame, scale = .75):
    # works for image, video and live video
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)

def rescaleLiveVideo(width, height):
    # works only for live video
    capture.set(3, width)
    capture.set(4, height)

## Resizing Image
img = cv.imread('C:/Users/Akash Ray/Desktop/fish_large.jpg')
resizedImg = rescaleFrame(img)

cv.imshow("image", img)
cv.imshow("resizedImg", resizedImg)

## Resizing Video
# capture = cv.VideoCapture('C:/Blender Projects/Coffee & Donut.mp4')
capture = cv.VideoCapture(1, cv.CAP_DSHOW)

while True:
    isTrue, frame = capture.read()
    resizedFrame = rescaleFrame(frame, scale = .7)

    cv.imshow("Video", frame)
    cv.imshow("resizedVideo", resizedFrame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
