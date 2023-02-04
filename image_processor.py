import cv2

img = cv2.imread("data/plant_pics/lavender.jpeg")
img = cv2.resize (img, (1024, 1024))
cv2.imwrite("lavender.png", img)