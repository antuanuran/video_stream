## "Video_stream"

### Основные поинты:

- [ ] WebRTC
- [ ] RTP - протокол
- [ ] ONVIF - протокол
- [ ] SOAP - протокол
- [ ] UDP - протокол 
- [ ] OpenCV (cv2), Pygame, PyAV, aioRTC, ZMQ, ImageZMQ - библиотеки
- [ ] YOLO - детекция объектов 
- [ ] Разобраться в захвате потока видео из ip-камеры на экран / браузер (как вариант библиотека OpenCV)
- [ ] Интеграция с FastAPI 




### Терминология:
- **WebRTC** (Web Real-Time Communications) - технология, которая позволяет Web-приложениям и сайтам захватывать и выборочно передавать аудио и/или видео медиа-потоки, а также обмениваться произвольными данными между браузерами
- **UDP** (User Datagram Protocol) - это протокол пользовательских датаграмм. С помощью UDP компьютерные приложения могут посылать сообщения (датаграммы) другим хостам по IP-сети без необходимости предварительного сообщения для установки специальных каналов передачи или путей данных.
- **RTP** (Real-time Transport Protocol) сетевой протокол, спроектированный для мультимедийных коммуникаций (VoIP, видеоконференции, телепрезентации), потоковой передачи мультимедиа (видео по запросу, прямые трансляции) и широковещательное медиа
- **ONVIF** (Open Network Video Interface Forum) - общепринятый протокол для совместной работы IP-камер, видеорегистраторов NVR, программного обеспечения, на случай, если все устройства разных производителей. Разработали АПИ-спецификации для интеграции продуктов безопасности между собой и объединили их в профили, содержащие конкретные наборы функций. Протокол **ONVIF** подробно описывает, как сетевые устройства передачи видео (IP-камеры, видеорегистраторы), интегрируются с сетевыми программами обработки и отображения видеопотока. 
- **YOLO** (You Only Look Once) — архитектура нейронных сетей, предназначенная для детекции объектов на изображении. Отличительной особенностью YOLO является подход к решению задачи детекции. Один из способов решения задачи детекции заключается в разбиении изображения на квадратные области, затем классификация этих областей на наличие объекта и классификация самого объекта
- **SOAP** (Simple Object Access Protocol) — стандартный протокол по версии W3C. Данные передаются в формате XML. В отличие от REST-протокола, где данные передаются в json.
- **Датаграмма** (datagram) - это блок информации, передаваемый протоколом через сеть связи без предварительного установления соединения и создания виртуального канала. Любой протокол, не устанавливающий предварительное соединение (а также обычно не контролирующий порядок приёмо-передачи и дублирование пакетов), называется датаграммным протоколом. Таковы, например, протоколы Ethernet, IP, UDP и др.

- https://habr.com/ru/articles/678706/ - поиск объектов
- https://dzen.ru/a/X8n9H2vK0Ey8ZBPF   - ImageAI
- https://youtu.be/Uj4O2_dwRiA?si=DppZU1Ls4EvOKc6g - ImageAI
- https://pythonpip.ru/osnovy/obnaruzhenie-i-raspoznavanie-obektov-v-python-s-pomoschyu-opencv - OpenCV
- https://pythonist-ru.turbopages.org/pythonist.ru/s/raspoznavanie-licz-i-dvizheniya-s-ispolzovaniem-kompyuternogo-zreniya/ - Opencv
- https://vc.ru/u/1389654-machine-learning/661520-osvoenie-opencv-s-pomoshchyu-python-polnoe-rukovodstvo-po-obrabotke-izobrazheniy-i-kompyuternomu-zreniyu - Opencv


### Описание процесса WebRTC:

#### Сокращенно:
  - 1.Захват камеры
  - 2.Кодирование (VP9)
  - 3.Запаковка в RTP-протокол
  - 4.Передача по сети пакетов через UDP
  - 5.Распаковка RTP
  - 6.Декодирование
  - 7.Получение MediaStream и связь с тегом в браузере

#### Развернуто:
- [x] **1. Захват камеры**:
  - есть некий API, который позволяет получить доступ к камере. 
  При этом мы не имеем возможности получить чистые байты, только - media stream. 
  - И дальше этот media stream нужно соединить с другим API.
  Учитывая, что видео состоит в среднем из 30 картинок в секунду, а каждая картинка весит около 1 мбайта, 
  то на выходе мы получаем необходимый битрейт (возможность обработки данных в единицу времени) более 30 мбайт в секунду или (***240 mbps***)
  Такая проходимость нереальна, поэтому необходимо сжимать (кодировать)

- [x] **2. Кодирование**:
  - jpeg - не подходит, т.к. сжатие не сильное (примерно 1 к 10) - **24 mbps**. 
  - Поэтому придумали другой способ сжатия - **VP9** (он сжимет примерно 1 к 200) - **1,5 mbps** вместо 240 mbps
  Суть его в том, что он определяет один главный кадр (***keyframe***) и далее определяет изменение относительно предыдущего кадра (***Дифф***)
  - Поэтому если потеряется один Дифф в середине, то дальше процесс может не пойти
  - И еще один важный момент, что ставка в этом кодировании идет на то, что изменение относительно небольшие между Диффами, но если же происходят резкие переходы (движения рукми в разные стороны), то могут происходить баги

- [x] **3. Запаковка в RTP**:
  - Для того, чтобы передать пакеты в сеть, они обворачиваются в Протокол **RTP**.
  - Данный протокол решает несколько задач, это: порядок пакетов (все пакеты должны идти получателю в том порядке, в котором они были отправлены), синхронизация времени аудио и видео-дорожек, правильное соединение дорожек между собой

- [x] **4. Передача пакетов по сети**:
  - Для передачи пакетов используется UDP - протокол (т.е. протокол без гарантий доставки пакетов в отличие от TCP)
  - За счет отсутствия гарантий, высокая скорость, т.к. пакеты отправляются все подряд по мере появления

- [x] **5. Распаковка RTP-протоколом**:
  - Протокол восстанавливает порядок пакетов и отправляет их в ***Декодер***

- [x] **6. Декодирование**:
  - Декодер уже наоборот расжимает обратно данные и собственно получаем тот самый ***MediaStream***, который изначально отправлялся с камеры одного пользователя на компьютер другого пользователя, который имеет доступ к данной камере.

- [x] **7. Воспроизведение**:
  - И в итоге мы прикручиваем данный ***MediaStream*** в HTML-разметку в тег 


### Дополнительно:
- [x] Для создания потокового видео на Python существует несколько библиотек, включая: OpenCV, Pygame, PyAV.
  - C помощью библиотеки **OpenCV** можно захватить видео с веб-камеры или из файла и отобразить его в окне приложения (cv2.VideoCapture(0).read())
- [x] Программы для ip-видеонаблюдения на ubuntu:
  - MotionEye, Xeoma, ZoneMinder

My ip-camera:
local ip-адрес: 192.168.1.166

My статический (белый) ip: 31.186.152.153



