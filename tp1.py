import cv2
import numpy as np 
try : 
    picture  = cv2.imread("image.png") 
    h,w,c = picture.shape
    imagRev=np.zeros(shape=picture.shape , dtype=np.uint16)
    imagRev = picture / 255.
    print(imagRev.dtype)
    cv2.imshow("reversed",imagRev)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception : 
    print("no image detected or wrong path")