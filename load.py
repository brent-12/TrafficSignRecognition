import os
import cv2

def loadData():
    images = []
    classNo = []
    newList = os.listdir("./train")

