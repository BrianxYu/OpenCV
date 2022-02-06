import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)


cv.waitKey(0)