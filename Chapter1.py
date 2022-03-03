import cv2

# Importing an image
# img = cv2.imread("Resources/test.jpeg")
# cv2.imshow("Output", img)
# cv2.waitKey(0)

# Import Video
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Resources/test_video.mp4")

while True:
    sucess, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Run Webcam
# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)

# while True:
#     sucess, img = cap.read()
#     img = cv2.resize(img, (frameWidth, frameHeight))
#     cv2.imshow("Result", img)
#     if cv2.waitKey(30) & 0xFF == ord('q'):
#         break
