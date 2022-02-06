import cv2 as cv



img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Cat', img)
 
# convert to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT) # ksize must be odd number
# cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny)

# dilating the image
dilated = cv.dilate(canny, (3, 3), iterations = 3)
# cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (3, 3), iterations = 3)
# cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
# cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped'. cropped)


cv.waitKey(0)