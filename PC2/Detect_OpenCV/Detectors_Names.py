import numpy as np
import matplotlib.pyplot as plt
import cv2
import pandas as pd
import glob2
import os
from mtcnn_cv2 import MTCNN
from time import time

def detectors_names():

    FILE_NAMES = glob2.glob('../detector_architectures/*.xml')

    NAMES_EXTRACTED = []

    for name in FILE_NAMES:
        n = name.split('/')[-1].split('.')[0]
        NAMES_EXTRACTED.append(n)

    DETECT_NAMES_DICT = dict(zip(FILE_NAMES, NAMES_EXTRACTED))
    DETECT_NAMES_DICT['MTCNN'] = 'MTCNN'
    return DETECT_NAMES_DICT

def main():
    DETECT_NAMES_DICT = detectors_names()

if __name__=="__main__":
    main()