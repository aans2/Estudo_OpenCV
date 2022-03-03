import cv2
import numpy as np

path = 'images/FOTO_6.jpeg'

img = cv2.imread(path)
imgResize = cv2.resize(img,(640,480))
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(imgResize)


# cv2.imshow("imgResize", imgResize)
# cv2.imshow("imgGray", imgGray)
# cv2.imshow("imgBlur", imgBlur)
cv2.imshow("imgCanny", imgCanny)
cv2.imshow("imgBlank", imgBlank)
cv2.waitKey(0)