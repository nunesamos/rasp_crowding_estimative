import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import glob2
import os
from mtcnn_cv2 import MTCNN
from datetime import datetime
from Detectors_Names import detectors_names
from Sender_Email import send_csv, send_image


def detect_faces(image_pth, plot_detected=True):
    fld = '../test_images/'
    images_pth = glob2.glob(fld + '*.jpg')

    image = cv2.imread(image_pth)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    fig = plt.figure(figsize=(9, 9))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.axis(False)

    DETECTORS = glob2.glob('../detector_architectures/*xml')
    image_with_detections = image.copy()


    for detec_path in DETECTORS:

        num_detections = 0

        face_cascade = cv2.CascadeClassifier(detec_path)
        faces = face_cascade.detectMultiScale(image, 1.2, 2)

        for (x, y, w, h) in faces:
            cv2.rectangle(image_with_detections, (x, y), (x + w, y + h), (255, 0, 0), 3)
            num_detections += 1

    plt.subplot(1, 2, 2)
    plt.imshow(image_with_detections)
    plt.axis(False)

    if plot_detected:
        plt.show()



def detect_faces_mtcnn(image_pth, plot_detected=True):

    NAMES_DICT = detectors_names()

    fld = '../test_images/'
    images_pth = glob2.glob(fld + '*.jpg')

    image = cv2.imread(image_pth)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    fig = plt.figure(figsize=(9, 9))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.axis(False)

    detector = MTCNN()
    image_with_detections = image.copy()
    result = detector.detect_faces(image)

    NAMES = ['MTCNN']
    CONT_DETECS = []

    if len(result) > 0:
        num_detcs = 0
        for res in result:
            x,y,w,h = res['box']
            keypoints = res['keypoints']
            cv2.rectangle(image_with_detections, (x, y), (x + w, y + h), (255, 0, 0), 3)
            num_detcs += 1

        CONT_DETECS.append(num_detcs)

        DETECTORS = glob2.glob('../detector_architectures/*.xml')

        for detec_path in DETECTORS:

            name = NAMES_DICT[str(detec_path)]
            NAMES.append(name)

            face_cascade = cv2.CascadeClassifier(detec_path)
            faces = face_cascade.detectMultiScale(image, 1.2, 2)

            num_detcs = 0
            for (x, y, w, h) in faces:
                cv2.rectangle(image_with_detections, (x, y), (x + w, y + h), (255, 0, 0), 3)
                num_detcs += 1

            CONT_DETECS.append(num_detcs)


    TRACK_DETECTS = dict(zip(NAMES, CONT_DETECS))

    plt.subplot(1, 2, 2)
    plt.imshow(image_with_detections)
    plt.axis(False)

    if plot_detected:
        plt.show()

    return TRACK_DETECTS

def get_mean_csv(pth, N=7):

    mean = 0

    csv_files_names = glob2.glob(pth + '*.csv')
    L = len(csv_files_names)

    if L>N:
        for i, fn in enumerate(csv_files_names[:N]):
            Data = pd.read_csv(fn).to_numpy()
            mean += Data.mean(axis=0)[-1]
    else:
        for i, fn in enumerate(csv_files_names):
            Data = pd.read_csv(fn).to_numpy()
            mean += Data.mean(axis=0)[-1]

    mean = mean/L
    return mean

def main():


    fld = '../test_images/'
    images_pth = glob2.glob(fld + '*.jpg')
    media = get_mean_csv('../CSV_files/', 5)
    print('Media de detecções: ', media)

    for i, image in enumerate(images_pth[-6:]):

        tr_d = detect_faces_mtcnn(image, plot_detected=False)

        if i==0:
            Column_Names = list(tr_d.keys())
            df = pd.DataFrame(columns=Column_Names)
            df.loc[i] = list(tr_d.values())
        else:
            df.loc[i] = list(tr_d.values())

        dtc_total = df.loc[i].sum()
        print('Detecções para {}  \n'.format(image), dtc_total)

        if dtc_total > media:
            send_image(image)


    df['TOTAL'] = df.sum(axis=1)

    dtm = datetime.now()
    df_path ='../CSV_files/{}_{}_{}_{}h{}min.csv'.format(dtm.year, dtm.month, dtm.day, dtm.hour, dtm.minute)
    df.to_csv(df_path)
    send_csv(df_path)




if __name__=="__main__":
    main()



