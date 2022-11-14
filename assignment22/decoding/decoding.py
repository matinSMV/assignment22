import cv2 as cv

img1 = cv.imread('img/a.tif', 0)
img2 = cv.imread('img/b.tif', 0)

result = img2 - img1

cv.imshow('result', result)
cv.imwrite('decoded.jpg', result)
cv.waitKey()