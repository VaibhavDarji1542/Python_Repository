import cv2 as cv
import sys
import google
 
img = cv.imread(r'/home/vaibhavdarji/Vaibhav/Machine_Learning /Tensorflow_Env/image.png')
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()