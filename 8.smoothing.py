import cv2 as cv

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# averaging smoothing: take average of surrounding kernel grids
avg = cv.blur(img, (3, 3))
cv.imshow('Average Blur', avg)

# Gauissian blur
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gauissian Blur', gaussian)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)
 