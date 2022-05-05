import matplotlib
import scipy
import numpy as np
import cv2
import matplotlib.pyplot as plt

# LOADING THE LOGO IMAGE (bright)
bright = cv2.imread('C:\\Users\Josephine\Downloads\logo.png')

# SEGMENTATION PROCESS:
# 1.Converting the img to HSV
brightHSV = cv2.cvtColor(bright,cv2.COLOR_BGR2HSV)

# 2.Getting the color values of color RED using paint application
bgr = [235, 42, 44]
# 3.Applying the threshold value for segmentation
thresh = 60
# 4.Convert 1D array to 3D, then convert it to HSV and take the first element or the HUE element
hsv = cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2HSV)[0][0]

# 5.Setting the minimum and maximum by subtract and add the threshold
minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])

# 6.Creating the mask
maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
# 7.Subtracting the mask from the original image
resultHSV = cv2.bitwise_and(bright, bright, mask=maskHSV)

# Plot Using OpneCV
cv2.imshow("Result HSV Blue.png",resultHSV)

# Converting the HSB to RGB
resultHSV1 = resultHSV[...,::-1]
#Ploting Using Matplot
plt.imshow(resultHSV1)
plt.show()

cv2.waitKey()

# The segmentation Process come from this:
# Sources: www.learnopencv.com/color-spaces-in-opencv-cpp-python/