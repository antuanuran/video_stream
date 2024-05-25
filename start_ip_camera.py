import os
import cv2

from main_functions import blur_face_function

USERNAME = "antuanuran"
PASSWORD = "651925"
# IP = "192.168.1.167"
IP = "31.186.152.153"
PORT = "554"

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

URL = f"rtsp://{USERNAME}:{PASSWORD}@{IP}:{PORT}/stream1"
print("Conectando com:" + URL)

capture = cv2.VideoCapture(URL, cv2.CAP_FFMPEG)

while True:
    ret, img = capture.read()

    img = blur_face_function(img)

    cv2.imshow("IP-CAMERA VIDEO", img)

    k = cv2.waitKey(20) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
