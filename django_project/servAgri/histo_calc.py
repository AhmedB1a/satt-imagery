import cv2
from matplotlib import pyplot as plt

def draw_image_histogram(image, channels, color='k'):
    hist = cv2.calcHist([image], channels, None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
    plt.savefig("C:/Users/Lenovo/Desktop/part2/images/")

def show_grayscale_histogram(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    draw_image_histogram(grayscale_image, [0])
    plt.show()

#---------------------------------------------------

def show_color_histogram(image):
    for i, col in enumerate(['b', 'g', 'r']):
        draw_image_histogram(image, [i], color=col)
    plt.title('Histogram')
    plt.xlabel("Pixels")
    plt.ylabel("Frequency")
    plt.savefig("C:/Users/Lenovo/Desktop/part2/images/tondvihisto.png")
    plt.show()

    #fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
    #ax.plot([0,1,2], [10,20,3])
    #fig.savefig('/home/nassim/Documents/PFE-M2-ADSI-2019/part2/to.png')





image = cv2.imread('C:/Users/Lenovo/Desktop/part2/images/ndvi-image.png')
show_color_histogram(image)
#show_grayscale_histogram(image)
#from servAgri.histo_calc import *