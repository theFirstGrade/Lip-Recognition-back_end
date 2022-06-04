# -*- coding: utf-8 -*-
import time

import cv2
import numpy as np
import pylab as pl
from PIL import Image
from PIL import ImageFilter
import os
import glob
import algorithms.code.Gabor_feature_extraction.Features as Features


def Gabor_h(HGamma, HKernelSize, HSig, HWavelength, mouth_centroid_x, mouth_centroid_y, i, ROIpath, shotname, GaborPath,
            SheetPath, FeaturesPath):
    # cur_dir2 = 'D:/codepython3/Gabor/' # path to store Gabor features

    if not os.path.exists(GaborPath):
        os.mkdir(os.path.join(GaborPath))
    Gaborpath = os.path.join(GaborPath, shotname)
    if not os.path.exists(Gaborpath):
        os.mkdir(Gaborpath)

    img = cv2.imread(ROIpath, 1)  # Loading color picture
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Change color picture into gray picture
    imgGray_f = np.array(imgGray, dtype=np.float32)  # Change data type of picture
    imgGray_f /= 255.

    # Parameters of horizontal filter
    orientationH = 90  # orientation of normal direction
    wavelengthH = HWavelength
    kernel_sizeH = HKernelSize
    sigH = HSig
    gmH = HGamma

    ps = 0.0
    thH = orientationH * np.pi / 180
    kernelH = cv2.getGaborKernel((kernel_sizeH, kernel_sizeH), sigH, thH, wavelengthH, gmH, ps)
    destH = cv2.filter2D(imgGray_f, cv2.CV_32F, kernelH)  # CV_32F
    Gabor_Path = Gaborpath + '/' + str('%02d' % i) + '.jpg'
    cv2.imwrite(Gabor_Path, np.power(destH, 2))

    Features.Features(mouth_centroid_x, mouth_centroid_y, i, shotname, Gabor_Path, SheetPath, FeaturesPath)
    # return i,shotname,Gabor_Path
