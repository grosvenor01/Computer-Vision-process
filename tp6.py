import cv2 
import numpy as np 

cv2.namedWindow("erode")
def erode_func():
    size = sizeErode*2+1
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(size , size))
    img_erode = cv2.erode(img , kernel)
    cv2.imshow("erode",img_erode)

def changeSize(x):
    global sizeErode
    sizeErode=x
    erode_func()

cv2.namedWindow("dilate")
def dilate_func():
    size = sizedilate*2+1
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(size , size))
    img_dilate = cv2.dilate(img , kernel)
    cv2.imshow("dilate",img_dilate)

def changeSize_dilate(x):
    global sizedilate
    sizedilate=x
    print(sizedilate)
    dilate_func()


cv2.namedWindow("morph")
def morph_func():
    size = sizemorph*2+1
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(size , size))
    img_morph = cv2.morphologyEx(img , cv2.MORPH_GRADIENT , kernel)
    cv2.imshow("morph",img_morph)

def morphSize(x):
    global sizemorph
    sizemorph=x
    morph_func()


img = cv2.imread("image.png" , cv2.IMREAD_GRAYSCALE)
cv2.threshold(img , 128 , 255, cv2.THRESH_BINARY,img)

sizeErode =1
cv2.createTrackbar("erodeSize" , "erode" , sizeErode , 17 , changeSize )

sizedilate = 1
cv2.createTrackbar("dilateSize" , "dilate" , sizedilate , 17 , changeSize_dilate )

sizemorph =1
cv2.createTrackbar("sizemorph" , "morph" , sizemorph, 17 , morphSize )

cv2.imshow("erode" , img)
cv2.imshow("dilate" , img)
cv2.imshow("morph" , img)
cv2.waitKey()
cv2.destroyAllWindows()