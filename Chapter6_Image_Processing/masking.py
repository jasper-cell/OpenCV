import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# 利用np.zeros加上原本图像的造型，能够很快的制造出一个与原图大小相同的mask
# 再利用cv2.rectangle等绘图功能，能够很方便的进行mask的改造
mask = np.zeros(image.shape[:2], dtype="uint8")
(cX, cY) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cX -75, cY-75), (cX+75, cY+75), 255, -1)
cv2.imshow("Mask", mask)

# 利用bitwise的各个操作运算来实现mask的功能
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("mask applied to image", masked)
cv2.waitKey(0)


mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (cX, cY), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

