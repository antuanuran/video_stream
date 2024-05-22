import cv2


def blur_face_function(img):
    face_cascade = cv2.CascadeClassifier(
        "files_all/haarcascade_frontalface_default.xml"
    )

    def blur_face(img):
        (h, w) = img.shape[:2]
        dW = int(w / 3.0)
        dH = int(h / 3.0)

        if dW % 2 == 0:
            dW -= 1
        if dH % 2 == 0:
            dH -= 1
        return cv2.GaussianBlur(img, (dW, dH), 0)

    faces = face_cascade.detectMultiScale(
        img, scaleFactor=2, minNeighbors=5, minSize=(20, 20)
    )  # Выделение лица. Возвращает массив лиц

    # массивы состоят из 4-х элементов: координаты x и y, затем идет ширина и высота блока, в кот. было обнаружено лицо
    for x, y, w, h in faces:
        cv2.rectangle(
            img, (x, y), (x + w, y + h), (0, 255, 0), 5
        )  # Начинаем рисовать: img - то, на чем мы будем рисовать и дальше уже координаты конца области
        img[y : y + h, x : x + w] = blur_face(img[y : y + h, x : x + w])
    return img


def color_function(img):
    # b = g = r = 0
    # clicked = False
    # def col_function(event, x, y, flags, param):
    #     if event == cv2.EVENT_LBUTTONUP:
    #         global b, r, g, clicked
    #         b, g, r = img[y, x]
    #         b = int(b)
    #         g = int(g)
    #         r = int(r)
    #         clicked = True
    #
    # cv2.namedWindow("Image")
    # cv2.setMouseCallback("Image", col_function)

    return img


def video_function(img):
    print("video frame..")
    return img
