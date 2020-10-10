import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# cv2,flip, 1代表水平翻转
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

#o代表垂直翻转
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# -1代表水平和垂直方向同时翻转
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

