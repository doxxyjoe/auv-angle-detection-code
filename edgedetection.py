import cv2
import numpy as np
font = cv2.FONT_HERSHEY_COMPLEX
x=cv2.imread('hd.jpg')
img_hsv=cv2.cvtColor(x, cv2.COLOR_BGR2HSV)

mask_low=np.array([0,50,20])
mask_upper=np.array([5,255,255])

mask_arrow=cv2.inRange(img_hsv, mask_low, mask_upper)
#edge=cv2.Canny(mask_arrow,50,150)
#cv2.imshow("canny",edge)
contours, hierarchy = cv2.findContours(mask_arrow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.02*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        

        if len(approx) == 7:
                cv2.putText(mask_arrow, "tip", (x, y), font, 1, (0, 255, 0))
cv2.imshow("canny",mask_arrow)                
cv2.waitKey(0)