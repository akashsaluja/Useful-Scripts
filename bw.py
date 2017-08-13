import fnmatch
import glob
import cv2
import os
import time

path = "/Users/akash/Desktop/"

current_milli_time = lambda: int(round(time.time() * 1000))
os.chdir(path)
scaleFactor = 1
directoryName = "screenshots/"
for file in glob.glob("Screen*.png"):
    print(file)
    if fnmatch.fnmatch(file, 'Screen*.png'):
        img = cv2.imread(file)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rows,cols, dim = img.shape
        img_gray = cv2.resize(img_gray,(int(cols/scaleFactor), int(rows/scaleFactor)), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(str(current_milli_time()) + "gray.png", img_gray, [cv2.IMWRITE_PNG_COMPRESSION, 9])
        os.rename(file, path+directoryName+file)