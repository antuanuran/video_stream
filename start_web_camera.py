import cv2

from main_functions import blur_face_function

capture = cv2.VideoCapture(0)

while True:
    ret, img = capture.read()

    img = blur_face_function(img)

    cv2.imshow("WEB-CAMERA VIDEO", img)

    k = cv2.waitKey(20) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()
