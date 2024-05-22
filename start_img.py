import cv2
from main_functions import color_function

img_path = "files_all/color.jpg"

capture = cv2.imread(img_path)

while True:
    img = color_function(capture)

    cv2.imshow("PHOTO", img)

    k = cv2.waitKey(30) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

cv2.destroyAllWindows()  # Убрать все окна
