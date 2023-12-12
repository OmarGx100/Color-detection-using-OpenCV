import cv2
import os
import numpy as np
from PIL import Image

#function to get the limits of a given color in the HSV color space
def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lower_limit = hsvC[0][0][0] - 10, 100, 100
    upper_limit = hsvC[0][0][0] + 10, 255, 255

    lower_limit = np.array(lower_limit, dtype= np.uint8)
    upper_limit = np.array(upper_limit, dtype = np.uint8)

    return lower_limit, upper_limit


cap = cv2.VideoCapture(0)
yellow = (0, 255, 255)
while True :
    ret, frame = cap.read() #unbacking the ret and the frames from the cam
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convdrting the frames to HSV COLOR SPACE 
    lower_limit, upper_limit = get_limits(yellow)     # getting the yellow "required color to detect" limits in the hsv color space
    mask = cv2.inRange(hsv_frame, lower_limit, upper_limit)  # masking the yellow pixels inside the frame
    mask_ = Image.fromarray(mask)                            # coverting the numpy frame array into a pillow object so we can draw our borders
    bbox = mask_.getbbox()                                   # border limits
    if bbox is not None :
        x1, y1, x2, y2 = bbox                               #unbacking the points of the border
        cv2.rectangle(frame, (x1,y1), (x2, y2),(255,0 , 0), 5)   # drawing the border across the yellow object in the frame
    cv2.imshow("my web cam", frame)                           # visualizing the web cam
    if cv2.waitKey(1) & 0xFF == ord('q'):                     # press 'q' to break the we cam visualizing 
        break
cap.release()                                       #release the memory and close all windows
cv2.destroyAllWindows()