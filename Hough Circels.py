import numpy as np
import cv2 as cv
img = cv.imread('Planets.jpg')
# output = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray1 = cv.medianBlur(gray, 5)

circles = cv.HoughCircles(gray1, cv.HOUGH_GRADIENT, 1, 220,
                          param1=140, param2=40, minRadius=0, maxRadius=0)  #2nd photo param1=80  param2 = 20   min-dist=200

detected_circles = np.uint16(np.around(circles))
for (x, y ,r) in detected_circles[0, :]:
    cv.circle(img, (x, y), r, (0, 0, 255), 4)
    cv.circle(img, (x, y), 5, (0, 255, 0), 3)


cv.imshow('output',img)
cv.waitKey(0)
cv.destroyAllWindows()