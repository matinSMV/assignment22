import cv2 as cv
import numpy as np

my_img = cv.imread('img/me.jpg', 0)
eq_img = cv.imread('img/eq.jpg', 0)

height, width = my_img.shape
eq_img = cv.resize(eq_img, (height, width))

merge1 = my_img//2 + eq_img//4
merge2 = my_img//4 + eq_img//2

result = np.zeros((height, width*4), dtype='uint8')

result[0:height, 0:width]=my_img
result[0:height, width:width*2]=merge1
result[0:height, width*2:width*3]=merge2
result[0:height, width*3:width*4]=eq_img

cv.imwrite('merged.jpg', result)