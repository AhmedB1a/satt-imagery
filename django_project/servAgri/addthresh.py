import numpy as np
import argparse
import cv2
from scipy.ndimage import label
import scipy.misc
from matplotlib import pyplot as plt

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
plt.imshow(image)
plt.title("La methode de Adaptative thresh blurred")
plt.show()
cv2.imshow("Image", image)

thresh = cv2.adaptiveThreshold(blurred, 255,
cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)
plt.imshow(thresh)
plt.title("La methode de Adaptative thresh mean")
plt.show()

thresh = cv2.adaptiveThreshold(blurred, 255,
cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
plt.imshow(thresh)
plt.title("La methode de Adaptative thresh gaussian")

plt.show()

#canny
image = cv2.imread(args["image"])
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
plt.imshow(canny)
plt.title("La methode de canny")
plt.show()

#watershed 


a = cv2.imread(args["image"])
a1 = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)
thresh,b1 = cv2.threshold(a1, 0, 255,
cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# since Otsu's method has over segmented the image
# erosion operation is performed
b2 = cv2.erode(b1, None,iterations = 2)
# distance transform is performed
dist_trans = cv2.distanceTransform(b2, 2, 3)
# thresholding the distance transform image to obtain
# pixels that are foreground
thresh, dt = cv2.threshold(dist_trans, 1,
255, cv2.THRESH_BINARY)
# performing labeling
#labelled = label(b, background = 0)
labelled, ncc = label(dt)
# labelled is converted to 32-bit integer
labelled = labelled.astype(np.int32)
# performing watershed
cv2.watershed(a, labelled)
#cv2.imshow("watershed", watshed)
# converting the ndarray to image
dt1 = scipy.misc.toimage(labelled)
# saving the image as watershed_output.png
dt1.show()

dt1.save('D:\careers\css bos\pn.png')
cv2.waitKey(0)