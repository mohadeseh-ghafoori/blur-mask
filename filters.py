import cv2 as cv 
img=cv.imread("G:\learn opencv/char.tif")
cv.imshow("original image", img)
#averaging
average=cv.blur(img,(3,3))
cv.imshow("average blur", average)
cv.waitKey(0)