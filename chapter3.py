import cv2
import numpy as np

img = cv2.imread("Resources/Tiger3.jpg")
print(img.shape)

imgResize = cv2.resize(img,(180,100))
imgCropped = img[0:100,100:200]

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.waitKey(0)

