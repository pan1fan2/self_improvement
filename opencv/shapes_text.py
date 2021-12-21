import cv2
import numpy as np

#hight,width,channel
img = np.zeros((512,512,3),np.uint8)
#img[:] = 255,0,0 # paint blue to the entire domain
#cv2.line(img,(0,0),(300,300),(0,255,0),3) 

#need to assign width(img.shape[0])first, create the diagonal line 
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) 

cv2.rectangle(img,(0,0),(250,350),(0,0,250),2)
# instead, choose to fill the rectangle
#cv2.rectangle(img,(0,0),(250,350),(0,0,250),cv2.FILLED)

cv2.circle(img,(400,40),30,(255,255,0),5)

cv2.putText(img,"Test",(300,200),cv2.FONT_HERSHEY_COMPLEX,1.5,(0,150,0),3)

cv2.imshow("Image",img)
cv2.waitKey(0)