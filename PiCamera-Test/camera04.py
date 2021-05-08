#!/usr/bin/env python3
import cv2 as cv
import numpy as np

img = cv.imread("/home/pi/Pictures/test01.jpg")
img = cv.resize(img, (600, 400))

imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgray, 127, 255, 0)
cv.imshow('imgray',imgray)

ret,thresh = cv.threshold(imgray,127,255,0)

im2, contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

cv.drawContours(img, contours, -1, (0,255,0), 3)

cv.imshow('mask',im2)

cv.imshow('contours',img)

k = cv.waitKey(0)

cv.destroyAllWindows()
