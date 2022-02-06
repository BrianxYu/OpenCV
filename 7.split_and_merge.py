import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('Boston', img)

# split the BGR image to corresponding component
b, g, r = cv.split(img)
# displayed as greyscale, lighter --> high concentration, darker --> little to no concentration
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

print(f'''
Original shape: {img.shape}
b: {b.shape}
g: {g.shape}
r:{r.shape}
''')

# merge back the image
merge = cv.merge([b, g, r])
cv.imshow('Merged', merge)

# see each individual component with actual color
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('B', cv.merge([b, blank, blank]))
cv.imshow('G', cv.merge([blank, g, blank]))
cv.imshow('R', cv.merge([blank, blank, r]))

cv.waitKey()