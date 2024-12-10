import cv2
import time
import numpy as np 
import math
"""
Recap: dans la detection d'un objet bla couleur on initiliser un cercle (le vert) fel fonction ta3na li rahou rayah 
yedi lacouleur li rahou hab ydectitha apres inRane function wahc dir thkam jmi3 coleur whdokhra w tdirlha mask a 1 w lokhrin dirlhom mask a
0 haka ydecti l'ojet 3la hssab lbyd li f tswira wela li nsouh countours b fonction findCountour 
ngetiw el circle li englobe le countours apres le tableaux : x , y , rayon , surface  ( tableau wsmou points )

"""
cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height =int(cap.get(4))
fourcc = cv2.VideoWriter.fourcc('X','V','I','D')
#out = cv2.VideoWriter("output2.avi" , fourcc, 34 ,(frame_width , frame_height))
lo=np.array([95 , 80 , 60]) 
hi=np.array([115 , 255 , 255])


def detect_inrange(image , surface_min , surface_max):
    points = []
    image = cv2.cvtColor(image , cv2.COLOR_BGR2HSV)
    image = cv2.blur(image , (5,5))
    mask = cv2.inRange(image , lo , hi )
    elements= cv2.findContours(mask , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)[-2]
    elements =sorted(elements , key=lambda x :cv2.contourArea(x) , reverse=True)
    for element in elements:
        if cv2.contourArea(element) >= surface_min and cv2.contourArea(element) < surface_max : 
            ((x,y) , rayon)=cv2.minEnclosingCircle(element)
            points.append(
                np.array([int(x),int(y),int(rayon) , int(cv2.contourArea(element))])
            )
    return image , mask , points

if not cap.isOpened():
    print("erreur")
    exit(0)

while(cap.isOpened()):
    ret , frame = cap.read()
    cv2.flip(frame,1 ,frame)
    image , mask , points = detect_inrange(frame , 200 , 300)
    cv2.circle(frame , (100,100) , 20 , (0,255 , 0) , 5)
    print(image[100 , 100])
    if(len(points)>0):
        cv2.circle(frame , (points[0][0] , points[0][1]), points[0][2] , (0 , 0 , 255))
        cv2.putText(frame , str(points[0][3]), (points[0][0] , points[0][1]),
                     cv2.FONT_HERSHEY_COMPLEX,1,(255 , 0 , 0) , 2 , cv2.LINE_AA
                    )
    if mask is not None:
        cv2.imshow("mask" , mask)
    cv2.imshow("image" , frame)
    if cv2.waitKey(10)& 0xff ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()