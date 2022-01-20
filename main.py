import cv2
import numpy
import collections
from glob import glob
from time import time

config_file = 'models/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'models/frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

class_labels = []
file_name = 'models/labels.txt'
with open(file_name, 'rt') as fpt:
    class_labels = fpt.read().rstrip('\n').split('\n')

model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

photos_path = glob("photos/*.jpg")

font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN
iterator = 0

for photo_file in photos_path:
    photo = cv2.imread(photo_file)
    start = time()
    ClassIndex, confidence, bbox = model.detect(photo, confThreshold=0.5)
    detection_time = time() - start
    iterator = iterator + 1
    for ClassInd, conf, boxes in \
            zip(ClassIndex.flatten(), confidence.flatten(), bbox):
        if ClassInd == 1:
            cv2.rectangle(photo, boxes, (255, 0, 0), 2)
            cv2.putText(
                photo,
                class_labels[ClassInd - 1],
                (boxes[0] + 5, boxes[1] + 20),
                font,
                fontScale=font_scale,
                color=(0, 0, 255),
                thickness=2
            )

    photo_number_text = f"Zdjecie nr {iterator}"
    person_count = collections.Counter(numpy.array(ClassIndex))[1]
    person_count_text = f"Liczba osob na zdjeciu: {person_count}"
    detection_time_text = f"Czas detekcji: {round(detection_time, 4)} sekund"
    title_text = f"{photo_number_text}. " \
                 f"{person_count_text}. " \
                 f"{detection_time_text}."
    print(photo_number_text)
    print(person_count_text)
    print(detection_time_text)
    cv2.imshow(title_text, photo)
    cv2.waitKey()
    cv2.destroyWindow(title_text)
