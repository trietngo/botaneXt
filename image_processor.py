import cv2

img = cv2.imread("potato.jpeg")
img = cv2.resize (img, (1024, 1024))
cv2.imwrite("potato.png", img)