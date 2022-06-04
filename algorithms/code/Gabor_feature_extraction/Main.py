import glob
import cv2
import os
import algorithms.code.Gabor_feature_extraction.ROI
import algorithms.code.Gabor_feature_extraction.Gabor
import algorithms.code.Gabor_feature_extraction.Features
import algorithms.code.Gabor_feature_extraction.Frame as Frame
import algorithms.code.Gabor_feature_extraction.Frame2 as Frame2
import dlib
import time


def aa(i):
    a = time.time()
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("algorithms/code/Gabor_feature_extraction/shape_predictor_68_face_landmarks.dat")
    Video_path = 'E:\\fyp_algorithm\\code\\code\\store\\video/*.mp4'
    Img_path = 'images/czh/'
    # PicturePath = 'E:\\fyp_algorithm\\code\\code\\store\\2Picture\\'  # path to store pictures
    PicturePath = 'algorithms/code/store/2Picture/'  # path to store pictures
    MouthPath = 'algorithms/code/store/2mouth/'  # path to store mouth
    GaborPath = 'algorithms/code/store/2Gabor/'  # path to store Gabor features
    SheetPath = 'algorithms/code/store/2Sheet/'  # path to storSheetPath
    FeaturesPath = 'algorithms/code/store/2Features/'  # path to store sheets
    # Frame.Frame(detector, predictor, Video_path, PicturePath, MouthPath, GaborPath, SheetPath, FeaturesPath)
    Frame2.Frame2(detector, predictor, i, Img_path, PicturePath, MouthPath, GaborPath, SheetPath, FeaturesPath)
    b = time.time()
    print("Time = ", b - a)

# if __name__ == '__main__':
#     aa()
