import cv2

img_path = "files_all/color.jpg"

img = cv2.imread(img_path)
b = g = r = 0
clicked = False


def color_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global b, r, g, clicked
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        clicked = True


cv2.namedWindow("IMAGE_MOUSE")
cv2.setMouseCallback("IMAGE_MOUSE", color_function)

while True:
    cv2.imshow("IMAGE_MOUSE", img)

    if clicked:
        cv2.rectangle(img, (20, 20), (700, 60), (b, g, r), -1)
        if b + g + r <= 350:
            cv2.putText(
                img,
                "R = " + str(r) + "; G = " + str(g) + "; B = " + str(b),
                (50, 50),
                2,
                1.0,
                (255, 255, 255),
            )
        else:
            cv2.putText(
                img,
                "R = " + str(r) + "; G = " + str(g) + "; B = " + str(b),
                (50, 50),
                2,
                1.0,
                (0, 0, 0),
            )

        clicked = False

    k = cv2.waitKey(30) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

cv2.destroyAllWindows()  # Убрать все окна
