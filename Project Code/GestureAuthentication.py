import cv2 as cv
import numpy as numpy
import math
import time
import os
import HandTrackingModule as htm

def rescaleCapture(width, height):
    capture.set(3, width)
    capture.set(4, height)


# Importing the graphics and storing them in a list to be accessed later on
graphicsList = os.listdir("Graphics")
headerList = []
for imgPath in graphicsList:
    header = cv.imread(f"Graphics/{imgPath}")
    headerList.append(header)
    
header = headerList[0]

capture = cv.VideoCapture(1, cv.CAP_DSHOW)
rescaleCapture(640, 480)
detector = htm.handDetector(detectionCon = 0.85)

while True:
    # 1. Show webcam window
    isTrue, frame = capture.read()
    frame = cv.flip(frame, 1)

    # 2. Track the hand
    frame = detector.findHands(frame)
    lmList = detector.findPosition(frame, draw=False)

    if len(lmList) != 0:
        print(lmList[4])

        # Tip of index finger and middle finger
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2 # centre point between both the finger
        length1 = math.hypot(x2-x1, y2-y1) # length between both finger
        
        # 3. Check if index finger is up
        fingers = detector.fingersUp()
        # print(fingers)

        # 3. Check whether it is 'secure' mode or 'access' mode by selection
        # Selection Gesture
        if length1 < 25:
            cv.circle(frame, (cx, cy), 15, (0, 255, 0), cv.FILLED)
            
            if cy < 67:
                if 10< cx < 100:
                    # we're back to menu
                    header = headerList[0] 
                elif 270 < cx < 350:
                    # we're in 'secure' mode : set the authentication
                    header = headerList[1]
                elif 550 < cx < 630:
                    # we're in 'access' mode : access the folder
                    header = headerList[2]


        # 4. Start drawing the pattern
        # 5. Store the pattern : set/check the authentication
        # 6. Check if pattern is matching
        # 7. Give access to folder/file

    # 8. Place the header
    frame[0:67, 0:640] = header
    cv.imshow("Webcam", frame)

    # Stop the program when 'x' is pressed
    if cv.waitKey(20) & 0xFF == ord('x'):
        break
