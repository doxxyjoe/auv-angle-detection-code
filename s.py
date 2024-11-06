import cv2  
import numpy as np

x=cv2.imread('hell.jpg')
img_hsv=cv2.cvtColor(x, cv2.COLOR_BGR2HSV)

mask_low=np.array([0,50,20])
mask_upper=np.array([5,255,255])

mask_arrow=(img_hsv, mask_low, mask_upper)

k=np.ones((5,5))

dilate=cv2.dilate(mask_arrow, k, iterations=2)
erode=cv2.erode(dilate, k, iterations=1)
a=cv2.bitwise_and(erode,x)
cv2.imshow("arrow detection", erode)
cv2.imshow("a",a)
cv2.waitKey(0)