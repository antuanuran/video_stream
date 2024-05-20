import cv2

# import numpy as np
# from mss import mss

capture = cv2.VideoCapture(3)

face_cascade = cv2.CascadeClassifier("files_all/haarcascade_frontalface_default.xml")

while True:
    ret, img = capture.read()

    faces = face_cascade.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5, minSize=(20, 20))       # Выделение лица. Возвращает массив лиц

    # Каждый масси состоит из 4-х элементов: координаты x и y. И дальше идет ширина и высота блока, в котором было обнаружено лицо
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 5) # Начинаем рисовать: img - то, на чем мы будем рисовать и дальше уже координаты конца области

    cv2.imshow("My Camera", img)    # Заголовок и сама картинка

    k = cv2.waitKey(30) & 0xFF              # Дождемся нажатия клавиши Esc
    if k == 27:
        break

capture.release()                           # перестать обращаться к камере
cv2.destroyAllWindows()                     # Убрать все окна
