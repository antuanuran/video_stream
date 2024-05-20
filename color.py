import cv2

img_path = "files_all/color.jpg"

img = cv2.imread(img_path)

while True:
    cv2.imshow("main", img)

    k = cv2.waitKey(30) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

cv2.destroyAllWindows()  # Убрать все окна
