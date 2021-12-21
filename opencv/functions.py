import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
kernel = np.ones((5,5),np.uint8)

# Gray Image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imgGray)

# Blur Image
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0)
cv2.imshow("Blurred Image",imgBlur)

#Edges detector
imgCanny = cv2.Canny(img,100,200) # 2 thresholds, high gradient, low gradient
cv2.imshow("Canny Image",imgCanny)

# Dialaton
imgDialation = cv2.dilate(imgCanny,kernel,iterations = 1)
cv2.imshow("Dialation Image",imgDialation)

# Erode
imgErode = cv2.erode(imgDialation,kernel,iterations = 1)
cv2.imshow("Eroded Image",imgErode)

cv2.waitKey(0)