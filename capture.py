import cv2


def blur_face(img):
    (h, w) = img.shape[:2]
    dW = int(w / 3.0)
    dH = int(h / 3.0)

    if dW % 2 == 0:
        dW -= 1
    if dH % 2 == 0:
        dH -= 1

    return cv2.GaussianBlur(img, (dW, dH), 0)


capture = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier("files_all/haarcascade_frontalface_default.xml")

# out = cv2.VideoWriter("files_all/output.mp4", cv2.VideoWriter_fourcc(*"MJPG"), 20.0, (1280, 720))

while True:
    ret, img = capture.read()

    faces = face_cascade.detectMultiScale(
        img, scaleFactor=2, minNeighbors=5, minSize=(20, 20)
    )  # Выделение лица. Возвращает массив лиц

    # массивы состоят из 4-х элементов: координаты x и y, затем идет ширина и высота блока, в кот. было обнаружено лицо
    for x, y, w, h in faces:
        cv2.rectangle(
            img, (x, y), (x + w, y + h), (0, 255, 0), 5
        )  # Начинаем рисовать: img - то, на чем мы будем рисовать и дальше уже координаты конца области
        img[y : y + h, x : x + w] = blur_face(img[y : y + h, x : x + w])

    # out.write(img)
    cv2.imshow("My Camera", img)  # Заголовок и сама картинка

    k = cv2.waitKey(30) & 0xFF  # Дождемся нажатия клавиши Esc
    if k == 27:
        break

# out.release()
capture.release()  # перестать обращаться к камере
cv2.destroyAllWindows()  # Убрать все окна
