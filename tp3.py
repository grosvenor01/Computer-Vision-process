import cv2 , numpy as np 
img = cv2.imread("image.png")
vois = 3 
def filtreMoy(img):
    h , w  , z= img.shape
    imgMoy = np.zeros(img.shape,np.uint8)
    for y in range(h):
        for x in range(w):
            if y < vois/2 or y>(h-vois/2)or x<vois/2 or x >(w-vois/2):
                imgMoy[y,x]=img[y,x]
            else :
                v2 = int(vois/2)
                imgVois = img[ int(y-v2):int(y+v2+1),int(x-v2):int(x+v2+1)]
                moy = 0
                for yv in range(imgVois.shape[0]):
                    for xv in range(imgVois.shape[1]):
                        moy +=imgVois[yv,xv]
                
                imgMoy[y,x]=np.mean(imgVois)
    return imgMoy


cv2.imshow("result1",img)
cv2.imshow("result",filtreMoy(img))
cv2.waitKey(0)
cv2.destroyAllWindows()