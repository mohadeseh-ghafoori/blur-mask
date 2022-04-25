import cv2 as cv 
import numpy as np
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
#masking
blank=np.zeros(img.shape[:2],dtype="uint8")
cicle=cv.circle(blank.copy(),(img.shape[0]//2,img.shape[1]//2),100,255,-1)
recrangle=cv.rectangle(blank.copy(),(150,150),(400,400),255,-1)
mask=cv.bitwise_and(cicle,recrangle)
masked_img=cv.bitwise_and(img,img,mask=mask)
cv.imshow("masked image", masked_img)
cv.waitKey(0)