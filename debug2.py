import cv2
import numpy as np
img = cv2.imread('hd.jpg')
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask_low=np.array([0,50,20])
mask_upper=np.array([5,255,255])


mask_arrow=cv2.inRange(img_hsv, mask_low, mask_upper)


k=np.ones((3,3))
erode=cv2.erode(mask_arrow,k,iterations=1)
dialate=cv2.dilate(erode,k,iterations=1)
contours, hierarchy = cv2.findContours(dialate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
     approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
     
     cv2.drawContours(dialate, contours, -1, (0, 255, 0),3)
for i, c in enumerate(contours):
     rect = cv2.minAreaRect(c)
     box = cv2.boxPoints(rect)
     box=np.int0(box)
    
     angle = int(rect[2])
     width = int(rect[1][0])
     height = int(rect[1][1])
     #if width < height:
     #angle = angle
     cv2.drawContours(dialate,[box],0,(0,0,255),2)
       

cv2.imshow("g",dialate)      
print(angle)
cv2.waitKey(0)