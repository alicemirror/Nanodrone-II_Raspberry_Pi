#!/usr/bin/env python3
import cv2 as cv
import numpy as np

img = cv.imread("/home/pi/Pictures/test01.jpg")
img = cv.resize(img, (600, 400))

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,50,150,apertureSize = 3)
lines = cv.HoughLines(edges,1,np.pi/180,200)

if(lines is None):
    print("No Lines Found")
else:
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    cv.imshow("Display window", img)

k = cv.waitKey(0)

cv.destroyAllWindows()
