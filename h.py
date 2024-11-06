import cv2
import numpy as np
import math as m

#def contourfig(source):
    
   # contours, hierarchy = cv2.findContours(source, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   # for cnt in contours:
    # approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

x=cv2.imread('hd.jpg')
img_hsv=cv2.cvtColor(x, cv2.COLOR_BGR2HSV)

mask_low=np.array([0,3,20])
mask_upper=np.array([5,255,255])

mask_arrow=cv2.inRange(img_hsv, mask_low, mask_upper)

k=np.ones((5,5))


erode=cv2.erode(mask_arrow, k, iterations=1)
dilate=cv2.dilate(erode, k, iterations=2)
cv2.imshow("arrow detection", dilate)
a=cv2.bitwise_and(x,x,mask= dilate)
gray_image = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
     approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
     if 2<len(approx)<8:
      cv2.drawContours(a, contours, -1, (0, 255, 0), 3)
for c in contours:
     # calculate moments for each contour
     M = cv2.moments(c)

     # calculate x,y coordinate of center
     if M["m00"] != 0:
         cX = int(M["m10"] / M["m00"])
         cY = int(M["m01"] / M["m00"])      
hull = []
 
# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))
    cv2.drawContours(a,hull,i,(255,0,0),4,8)  
rows,cols = a.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(a,(cols-1,righty),(0,lefty),(0,255,0),2) 
#ang= m.atan((righty-lefty)/(cols-1))
cv2.line(a, (cX, cY), (cX, cY-500), (100, 255, 100), thickness=3)   
x_axis=np.array([-1,0])    
line_=np.array([vx,vy])
dot_product=np.dot(x_axis,line_)
angle_with_xaxis=np.arccos(dot_product)*180/m.pi-90
#resize=cv2.resize(a,(800,800))
print(len(contours))
print(cX,",",cY)
print(angle_with_xaxis)
cv2.circle(a, (cX, cY), 2, (255, 255, 255), -1)
cv2.imshow("a",a)
cv2.waitKey(0)