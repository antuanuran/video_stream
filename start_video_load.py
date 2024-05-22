import cv2
from main_functions import video_function

img_path = "files_all/video_cats.mp4"

capture = cv2.VideoCapture(img_path)

if not capture.isOpened():
    print("Error opening video stream or file")

else:
    fps = capture.get(cv2.CAP_PROP_FPS)
    print("FPS: ", fps)

    frame_count = capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("Frame count: ", frame_count)

    file_count = 0

    while True:
        ret, img = capture.read()

        img = video_function(img)
        cv2.imshow("PHOTO", img)

        k = cv2.waitKey(30) & 0xFF  # Дождемся нажатия клавиши Esc
        if k == 27:
            break

    capture.release()
    cv2.destroyAllWindows()  # Убрать все окна
