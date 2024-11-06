import cv2  
import numpy as np
for eps in np.linspace(0.001, 0.05, 10):
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, eps * peri, True)
	# draw the approximated contour on the image
	output = image.copy()
	cv2.drawContours(output, [approx], -1, (0, 255, 0), 3)
	text = "eps={:.4f}, num_pts={}".format(eps, len(approx))
	cv2.putText(output, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,
		0.9, (0, 255, 0), 2)
	# show the approximated contour image
	print("[INFO] {}".format(text))
	cv2.imshow("Approximated Contour", output)
	cv2.waitKey(0)