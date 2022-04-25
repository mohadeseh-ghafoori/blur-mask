import cv2 as cv 
img=cv.imread("G:\learn opencv/char.tif")
cv.imshow("original image", img)
#averaging
average=cv.blur(img,(7,7))
cv.imshow("average blur", average)
#Gaussian filter
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian blur", gauss)
cv.waitKey(0)