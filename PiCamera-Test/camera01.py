#!/usr/bin/env python3
import cv2 as cv
import sys
img = cv.imread("/home/pi/Pictures/test01.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("/home/pi/Pictures/test01.png", img)
