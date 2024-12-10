import cv2
import time
cap = cv2.VideoCapture("https://192.168.137.244:8080/video")
frame_width = int(cap.get(3))
frame_height =int(cap.get(4))
fourcc = cv2.VideoWriter.fourcc('X','V','I','D')
out = cv2.VideoWriter("output2.avi" , fourcc, 34 ,(frame_width , frame_height))
if not cap.isOpened():
    print("erreur")
    exit(0)

while(cap.isOpened()):
    ret , frame = cap.read()
    t_start = time.time()
    if not ret :
        print("erreur read the frame")
        break
    out.write(frame)
    cv2.imshow("image" ,  frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
    t_fin = time.time()
    print(t_fin-t_start)
cap.release()
out.release()
cv2.destroyAllWindows()