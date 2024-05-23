import cv2

capture = cv2.VideoCapture(0)

b = g = r = 0
clicked = False


def color_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        global b, r, g, clicked
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)
        print(b, g, r)
        clicked = True

    if event == cv2.EVENT_RBUTTONUP:
        print("вы нажали правую кнопку")
        clicked = False


cv2.namedWindow("IMAGE_MOUSE")
cv2.setMouseCallback("IMAGE_MOUSE", color_function)

while True:
    ret, img = capture.read()
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

        cv2.imshow("IMAGE_MOUSE", img)

    k = cv2.waitKey(30) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

capture.release()
cv2.destroyAllWindows()  # Убрать все окна
