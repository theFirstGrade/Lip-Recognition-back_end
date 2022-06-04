# -*- coding: utf-8 -*-
import glob
import time

import cv2
import os
import algorithms.code.Gabor_feature_extraction.ROI as ROI
import algorithms.code.Gabor_feature_extraction.TPE as TPE


def Frame2(detector, predictor, i, Img_path, PicturePath, Mouth_path, GaborPath, SheetPath, FeaturesPath):
    # if not os.path.exists(PicturePath):
    #     os.mkdir(os.path.join(PicturePath))
    # print(VideoPath)
    # for video in glob.glob(VideoPath):  # path of videos
    #     print(video)
    #     (filepath, tempfilename) = os.path.split(video)
    #     (shotname, extension) = os.path.splitext(tempfilename)
    # folder_name = i
    # Path = os.path.join(folder_name)
    # if not os.path.exists(Path):
    #     os.mkdir(Path)
    #
    #     cap = cv2.VideoCapture(video)
    #     fps = cap.get(cv2.CAP_PROP_FPS)
    #     size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    #     # size=(960,544)
    #     # print 'size',size
    #     print(1111111111111111111111111)
    #     i = 0
    #     while (cap.isOpened()):  # cv2.VideoCapture.isOpened()
    #         a = time.time()
    #         i = i + 1
    #         ret, frame = cap.read()  # cv2.VideoCapture.read()　
    #
    #         print("frame1 = ", time.time() - a)
    #         a = time.time()
    #
    #         if i >= 1:
    #             if ret == True:
    #                 path = Path + '/'
    #                 picturepath = path + str('%02d' % i) + '.jpg'
    #                 # print picturepath
    #                 cv2.imwrite(picturepath, frame)
    #                 print("frame2 = ", time.time() - a)
    #                 # a = time.time()
    #
    #                 ROI.rect1(detector, predictor, i, shotname, picturepath, Mouth_path, GaborPath, SheetPath,
    #                           FeaturesPath)
    #                 # print("Time3 = ", time.time() - a)
    #                 # a = time.time()
    #
    #                 if cv2.waitKey(1) & 0xFF == ord('q'):
    #                     break
    #                 # print("Time4 = ", time.time() - a)
    #
    #             else:
    #                 break
    #
    #     cap.release()

    ROI.rect1(detector, predictor, i, 'czh', PicturePath + 'czh/' + str(i) + '.jpg', Mouth_path, GaborPath, SheetPath,
              FeaturesPath)
