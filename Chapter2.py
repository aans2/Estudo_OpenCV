import cv2
import numpy as np

img = cv2.imread("Resources/camila.jpeg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (3,3),0)
imgCanny = cv2.Canny(imgBlur, 100, 150)

kernel = np.ones((5,5), np.uint8)
imgDia = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDia, kernel, iterations=1)

cv2.imshow("Image", img)
cv2.imshow("Image Gray", imgGray)
cv2.imshow("Image Blur", imgBlur)
cv2.imshow("Image Canny", imgCanny)
cv2.imshow("Image Dia", imgDia)
cv2.imshow("Image Erode", imgErode)
cv2.waitKey(0)