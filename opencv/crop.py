import cv2

img = cv2.imread("Resources/lambo.png")

# height first then width,recall that in image resize, width comes first~  see resize.py
imgCropped = img[0:200,300:800]

cv2.imshow("Image",img)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)