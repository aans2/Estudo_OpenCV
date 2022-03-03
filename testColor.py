import cv2
import numpy as np

def empty(a):
    pass

path = 'images/FOTO_6.jpeg'

# Create trackbars
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)
cv2.createTrackbar("Hue min", "TrackBars",0,179, empty)
cv2.createTrackbar("Hue max", "TrackBars",94,179, empty)
cv2.createTrackbar("Sat min", "TrackBars",59,255, empty)
cv2.createTrackbar("Sat max", "TrackBars",255,255, empty)
cv2.createTrackbar("Val min", "TrackBars",000,255, empty)
cv2.createTrackbar("Val max", "TrackBars",255,255, empty)

def getContours(img):
    aux = 0
    countours, herarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    print(len(countours))
    for cnt in countours:
        area = cv2.contourArea(cnt)
        # print(area)
        cv2.drawContours(imgCountour, cnt,-1,(255,0,0),3)
        peri = cv2.arcLength(cnt, True)
        # print(peri)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
        # print(len(approx))
        objCor = len(approx)
        x, y, w, h = cv2.boundingRect(approx)

        cv2.rectangle(imgCountour, (x,y), (x+w,y+h),(0,255,0),2)



while True:

    img = cv2.imread(path)
    imgResize = cv2.resize(img,(640,480))
    imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
    imgCountour = imgResize.copy()

    # Get trackbars values
    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val max", "TrackBars")

    # print(h_min,h_max,s_min,s_max,v_min,v_max)

    # Define range
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    # Define mask
    mask = cv2.inRange(imgHSV, lower, upper)

    # Get image shape
    imgCanny = cv2.Canny(mask,50,50)

    # get countours
    getContours(imgCanny)

    # compare two image and apply mask
    imgResult = cv2.bitwise_and(imgResize, imgResize,mask=mask)

    # stack images horizontal
    imgHor = np.hstack((imgResize,imgResult))


    cv2.imshow("imgCanny", imgCanny)
    cv2.imshow("imgCountour", imgCountour)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("result", imgHor)
    cv2.waitKey(1)