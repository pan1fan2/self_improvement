import cv2

# Image
# img = cv2.imread("Resources/lena.png")
# cv2.imshow("Output",img)
# cv2.waitKey(0)

# Saved video
# cap = cv2.VideoCapture("Resources/testVideo.mp4")
# while True:
#     sucess,img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF == ord('q'): # delay + press q to exit
#         break

# live video from build-in cam
cap = cv2.VideoCapture(0) # 0 : cam id, build in cam
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) # set width
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # set height
#cap.set(10,100) # set brightness
#cap.set(cv2.CAP_PROP_BRIGHTNESS,100)
while True:
    sucess,img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'): # delay + press q to exit
        break