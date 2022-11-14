import cv2 as cv

origin = cv.imread('img/board - origin.bmp', 0)
test = cv.imread('img/board - test.bmp', 0)

test_flipH = cv.flip(test, 1)


result = cv.absdiff(origin, test_flipH)

cv.imwrite('board-diferrence.jpg', result)