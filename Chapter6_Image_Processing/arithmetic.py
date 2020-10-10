from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

print("max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))
print("warp around: {}".format(np.uint8([200])+np.uint8([100])))
print("warp around: {}".format(np.uint8([50])- np.uint8([100])))

# numpy的uint8运算和opencv的uint8运算的规则是不同的
M = np.ones(image.shape, dtype="uint8")*100
added = cv2.add(image, M)
cv2.imshow("Added", added)

M = np.ones(image.shape, dtype="uint8") * 50
substracted = cv2.subtract(image, M)
cv2.imshow("Substracted", substracted)
cv2.waitKey(0)





