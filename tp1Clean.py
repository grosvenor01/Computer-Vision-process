import cv2
import numpy as np 
def Load_show():
    try : 
        picture  = cv2.imread("image.png")
        print(picture)
        cv2.imshow('image' , picture)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception : 
        print("no image detected or wrong path")

def Rverse():
     #create new picture with old one's shape 
        picture  = cv2.imread("image.png")
        h,w,c = picture.shape
        imagRev=np.zeros(shape=picture.shape , dtype=np.uint8)
        #method  
        for y in range(h):
            for x in range(w):
                imagRev[y,x,:]=255 - picture[y,x,:]
        #method2
        imagRev = 255 - picture
        cv2.imshow("reversed",imagRev)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

#generale infos
data = picture.shape
type = picture.dtype
print(data , type )

# comment changer le type de valeu d'image et corriger l'image 