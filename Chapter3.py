import cv2
import numpy as np

img = cv2.imread("Resources/camila.jpeg")
print(img.shape)

imgResize1 = cv2.resize(img, (640,480))
imgResize2 = cv2.resize(img, (0,0), None,0.5,0.5)
print(imgResize2.shape)

imgCrop = img[50:375, 220:520]

cv2.imshow("Image", img)
cv2.imshow("Image Resize 1", imgResize1)
cv2.imshow("Image Resize 2", imgResize2)
cv2.imshow("Image Crop", imgCrop)
cv2.waitKey(0)
