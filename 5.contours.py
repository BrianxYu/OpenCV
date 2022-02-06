import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
img2 = cv.drawContours(img, contours, -1, (0, 255, 0), 2)
cv.imshow('Contour', img2)

cv.waitKey(0) 