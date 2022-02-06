import cv2 as cv

# read images
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('cat', img)
# cv.waitKey(0) # waits for a key press, 0 means indefinitely

# read video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue: break
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()








