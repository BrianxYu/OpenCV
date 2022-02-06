import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
width, height = blank.shape[:2]

cv.imshow('Blank', blank)

# 1. paint image to certain color
# blank[:] = 0,0,255
# cv.imshow('Red', blank)

# 2. draw rectangle
cv.rectangle(blank, (0, 0), (width//2, height//2), (0, 255, 0), thickness = -1)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (width//2, height//2), 40, (0, 0, 255), thickness = -1)
cv.imshow('Circle', blank)

# 4. draw a line
cv.line(blank, (0, 0), (width//2, height//2), (255, 255, 255), thickness = 3)
cv.imshow('Line', blank)

# 5. write text
cv.putText(blank, 'Hello', (width//2, height//2), cv.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), thickness = 2)
cv.imshow('Text', blank)

cv.waitKey(0)