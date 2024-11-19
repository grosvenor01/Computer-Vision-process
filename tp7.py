import cv2
import numpy as np 

img = cv2.imread("image.png" , cv2.IMREAD_COLOR)
# if we used : img_b = np.zeros(img.shape[:2] , img.dtype) this recieve the colors as niveau de gris ()
# couldn't 
img_b = np.zeros(img.shape , img.dtype)
img_g = np.zeros(img.shape , img.dtype)
img_r = np.zeros(img.shape , img.dtype)

h,w , c = img.shape

"""for y in range(h):
    for x in range(w):
        img_b[y , x , 0] = img[y , x , 0]
        img_g[y , x , 1] = img[y , x , 1]
        img_r[y , x , 2] = img[y , x , 2]
"""
img_b[:h , :w , 0] , img_g[:h , :w , 1]  , img_r[:h , :w , 2]  = [ img[:h , :w , i] for i in range(3) ]


cv2.imshow("img_b", img_b)
cv2.imshow("img_g", img_g)
cv2.imshow("img_r", img_r)

""" to cast img to grey from a bgr format we should sum up all the images with each channel color and multiply by 1/3 
becasue we have 3 colors and to avoid the case where the sum been bigger than the maximum number of this type 255
bcs it gonna be trancated """


""" manual converting :
grey_img  = (img_b[...,0]*0.33 +img_g[...,1]*0.33+img_r[...,2]*0.33)/(3*255)
cv2.imshow("img_r", grey_img)
"""
img_hsv = cv2.cvtColor(img , cv2.COLOR_BGR2HSV)
cv2.imshow("img_hsv", img_hsv)

# Conversion de type
new_img_float =  np.float32(img/255)
new_img_int =  np.uint16(new_img_float*(255*255-1))
cv2.imshow("img_float", new_img_float)
cv2.imshow("img_int", new_img_int)
cv2.waitKey()
cv2.destroyAllWindows()