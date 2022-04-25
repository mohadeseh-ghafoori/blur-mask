import cv2 as cv 
img=cv.imread("G:\learn opencv/char.tif")
cv.imshow("original image", img)
#averaging
average=cv.blur(img,(7,7))
cv.imshow("average blur", average)
#Gaussian filter
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow("Gaussian blur", gauss)
#median 
median=cv.medianBlur(img,7) 
cv.imshow("median blur", median)
#bilateral filter
bilateral=cv.bilateralFilter(img,20,160,150) #blur image but keeps edges fairly sharp 
cv.imshow("bilateral filter blur", bilateral)
cv.waitKey(0)