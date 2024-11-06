import cv2
import numpy as np
x=cv2.imread('hd.jpg')
img_hsv=cv2.cvtColor(x, cv2.COLOR_BGR2HSV)

mask_low=np.array([0,50,20])
mask_upper=np.array([5,255,255])

mask_arrow=cv2.inRange(img_hsv, mask_low, mask_upper)

k=np.ones((5,5))

#dilate=cv2.dilate(mask_arrow, k, iterations=2)
#erode=cv2.erode(dilate, k, iterations=1)
output_bilateral=cv2.bilateralFilter(mask_arrow, 5,10,10)
cv2.imshow("arrow detection",output_bilateral) 
a=cv2.bitwise_and(x,x,mask= output_bilateral)
gray_image = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
     cv2.drawContours(a,contours,-1,(0,255,255),3)

     
     approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
     if 2<len(approx)<8:
      cv2.drawContours(a, contours, -1, (0, 255, 0), 3)
      #cv2.drawContours(a,contours,-1,(0,255,255),3)

print(len(contours))
cv2.imshow("a",a)
cv2.waitKey(0)