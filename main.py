import cv2
import numpy as np
from PIL import Image


from util import get_limits


yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)

    mask = cv2.inRange(hsvImg, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, w, h = bbox
        
        frame = cv2.rectangle(frame, (x1,y1), (w,h), (0, 255, 0), 3)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()