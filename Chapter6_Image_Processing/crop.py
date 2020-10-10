import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# crop就是从原始图像中选出最care的部分，利用numpy的slice功能
cropped = image[30:120, 240:335]
cv2.imshow("Rex Face", cropped)
cv2.waitKey(0)

