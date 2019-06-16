import matplotlib.pyplot as plt
import numpy as np
import cv2

from skimage.measure import compare_ssim as ssim
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
ap.add_argument("-t", "--third", required = True,
help = "Path to the third image")
ap.add_argument("-s", "--second", required = True, help="path to the second image")

args = vars(ap.parse_args())

# construct the argument parse and parse the arguments
""" ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="first input image")
ap.add_argument("-s", "--second", required=True,
	help="second")
args = vars(ap.parse_args()) """

""" # load the two input images
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"]) """
 
""" # convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY) """

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err
 
def compare_images(imageA, imageB, title):
	# compute the mean squared error and structural similarity
	# index for the images
	m = mse(imageA, imageB)
	s = ssim(imageA, imageB)
 
	# setup the figure
	fig = plt.figure(title)
	plt.suptitle("MSE: %.2f, SSIM: %.2f" %(m, s))
 
	# show first image
	ax = fig.add_subplot(1, 2, 1)
	plt.imshow(imageA, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show the second image
	ax = fig.add_subplot(1, 2, 2)
	plt.imshow(imageB, cmap = plt.cm.gray)
	plt.axis("off")
 
	# show the images
	plt.show()


#args["first"]
#original = cv2.imread("D:/careers/python-my-projects/django/project-code/django_project/server2/django_project/servAgri/output/ndvi-image.png")
#contrast = cv2.imread("D:/careers/python-my-projects/django/project-code/django_project/server2/django_project/servAgri/output/ndvi-image.png")
#shopped = cv2.imread("D:/careers/python-my-projects/django/project-code/django_project/server2/django_project/servAgri/output/sr-image.png")
 
original = cv2.imread(args["image"])
contrast = cv2.imread(args["second"])
shopped = cv2.imread(args["third"])
 
# convert the images to grayscale
original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
contrast = cv2.cvtColor(contrast, cv2.COLOR_BGR2GRAY)
shopped = cv2.cvtColor(shopped, cv2.COLOR_BGR2GRAY)

# initialize the figure
fig = plt.figure("Images")
images = ("image A", original), ("image B", contrast), ("image B", shopped)
 
# loop over the images
for (i, (name, image)) in enumerate(images):
	# show the image
	ax = fig.add_subplot(1, 3, i + 1)
	ax.set_title(name)
	plt.imshow(image, cmap = plt.cm.gray)
	plt.axis("off")
 
# show the figure
plt.show()

""" # compare the images
compare_images(imageA, imageB, "Image A vs. Image B")
#compare_images(imageA, imageA, "Image A vs. Image A") """



compare_images(original, original, "Original vs. Original")
compare_images(original, contrast, "Original vs. Contrast")
compare_images(original, shopped, "Original vs. Photoshopped")