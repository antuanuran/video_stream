import cv2
import numpy as np
from mss import mss


capture = cv2.VideoCapture(3)

while True:
    ret, img = capture.read()

    cv2.imshow('From Camera', img)

    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
