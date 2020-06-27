import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
print(img)
# img[:]=255,0,0

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)    to fill the rectangle with color
cv2.circle(img,(400,180),40,(255,255,0),4)
cv2.putText(img," Open CV ",(310,120),cv2.FONT_ITALIC,1,(255,255,0),3)

cv2.imshow("Image",img)
cv2.waitKey(0)
