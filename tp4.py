""" 5 types de seuillage exist sur la fonction 
1. binary : si SRC(x,y) > seuil  , DIST(x,y)=MaxValue else DIST(x)=0
2. binary_inv si SRC(x,y) > seuil , DIST(x,y)=0 else = MAX_value
3. Trunc si SRC(x,y) > seuil , DIST(x,y) = seuil , sinon DIST = SRC
4. tozero si  SRC(x,y) > seuil , DIST(x,y)=SRC(x,y) sinon =0
5. tozero iverse 
"""

import cv2 
import numpy as np 

img = cv2.imread("image.png" , cv2.IMREAD_GRAYSCALE)
th = 128 
thresh_type=0
def afficher():
    grad_x = img[:,:img.shape[1]-1]-img[:,1:]
    grad_y = img[:img.shape[0]-1,:]-img[1:,:]

    new_column = np.full((grad_x.shape[0], 1), 255)
    grad_x = np.concatenate((grad_x, new_column), axis=1)

    new_row = np.full((1, grad_y.shape[1]), 0)
    grad_y = np.concatenate((grad_y, new_row), axis=0)

    # lazem seuillage 
    magnitude = np.sqrt(grad_x**2 + grad_y**2)
    magnitude = magnitude.astype(np.uint8)

    the = 200
    sup_th_img = img > the # treturni array of bool ( mask )
    sub_th_img = img < the
    magnitude[sup_th_img]=255
    magnitude[sub_th_img]=0
    
    imgRes = np.zeros_like(magnitude, dtype=np.uint8)
    sup_th_img = img > th # treturni array of bool ( mask )
    sub_th_img = img < th
    if thresh_type == 0:
        imgRes[sup_th_img]=255
        imgRes[sub_th_img]=0
    elif thresh_type == 1:
        imgRes[sup_th_img]=0
        imgRes[sub_th_img]=255
    elif thresh_type==2:
        imgRes[sup_th_img]=th
        imgRes[sub_th_img]=img[sub_th_img]
    elif thresh_type ==3:
        imgRes[sup_th_img]=img[sup_th_img]
        imgRes[sub_th_img]=0
    elif thresh_type==4:
        imgRes[sup_th_img]=0
        imgRes[sub_th_img]=img[sub_th_img]
    cv2.threshold(magnitude , th , 255 , thresh_type , imgRes)
    cv2.imshow("img2",img)
    cv2.imshow("img" , imgRes)
def change_th(x):
    global th 
    th=x
    afficher()
def change_type(x):
    global thresh_type
    thresh_type = x
    afficher()
afficher()
cv2.createTrackbar("thresh" , "img" , 0,255 ,change_th)
cv2.createTrackbar("type" , "img" , 0,4 ,change_th)
cv2.waitKey(0)
cv2.destroyAllWindows()