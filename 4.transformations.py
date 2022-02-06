import cv2 as cv
import numpy as np



img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# Transformation
def translate(image, x, y):
    '''
        translate the image
        -x --> left
        x --> right
        -y --> up
        y --> down
    '''
    transMat = np.float32([[1, 0, x],
                           [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])

    return cv.warpAffine(image, transMat, dimensions)

# translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)

# Rotation
def rotate(image, angle, rotPoint = None):
    height, width = image.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(image, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0) # flipcode: 0: vertically, 1: horizontally, -1: both way
cv.imshow('Flipped', flip)

# cropping
cropped = img[200: 400, 300: 400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)