import cv2
from matplotlib import pyplot as plt

def draw_image_histogram(image, channels, color='k'):
    hist = cv2.calcHist([image], channels, None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
    #plt.savefig("D:/careers/python-my-projects/django/project-code/django_project/server2/django_project/servAgri/output/histo_out/")

def show_grayscale_histogram(image):
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    draw_image_histogram(grayscale_image, [0])
    plt.show()

#---------------------------------------------------

def show_color_histogram(image):
    for i, col in enumerate(['b', 'g', 'r']):
        draw_image_histogram(image, [i], color=col)
    plt.title('Histogram of the indices')
    plt.xlabel("Pixels")
    plt.ylabel("Frequency")
    plt.savefig("D:\\careers\\python-my-projects\\django\\project-code\\django_project\\server2\django_project\\servAgri\\output\\histo_out\\default_histo.png", \
        dpi=200, bbox_inches='tight', pad_inches=0.7)
    #plt.show()

    #fig, ax = plt.subplots( nrows=1, ncols=1 )  # create figure & 1 axis
    #ax.plot([0,1,2], [10,20,3])
    #fig.savefig('/home/nassim/Documents/PFE-M2-ADSI-2019/part2/to.png')







# image = cv2.imread('C:/Users/Lenovo/Desktop/part2/images/ndvi-image.png')
# show_color_histogram(image)
#show_grayscale_histogram(image)
#from servAgri.histo_calc import *
#from servAgri.histo_calc import *

""" 
def get_ix(index):
    import time 
    #time.sleep(25)
    img_path = 'D://careers//python-my-projects/django//project-code//django_project//server2//django_project//servAgri//output//histo_out//' + index + '-image.png'
    #print('the path;',img_path)
    img_arr = cv2.imread(img_path)
    # ""     import time
    # time.sleep(5)  "" 
    #show_color_histogram(img_arr)
    chans = cv2.split(img_arr)
    colors = ("b", "g", "r")
    plt.title("kdfjdkfj")
    plt.xlabel("labelx")
    plt.ylabel("ylabel")

    for (chan, color) in zip(chans, colors):
        hist = cv2.calcHist([chan], [0], None, [256], [0,256])
        plt.plot(hist, color = color)
        plt.xlim([0,256])
        # plt.savefig("D://careers//python-my-projects//django//project-code//django_project//server2//django_project//servAgri//output//histo_out//" + index + "-histo.png")
        print('ok ' + chan +  color)
    plt.savefig("D://careers//python-my-projects//django//project-code//django_project//server2//django_project//servAgri//output//histo_out//" + index + "-histo.png")
 """

def get_ix(index):
    img_path = 'D://careers//python-my-projects/django//project-code//django_project//server2//django_project//servAgri//output//' + index + '-image.png'
    img_arr = cv2.imread(img_path)
    #cv2.imshow("the original image",img_arr)
    chans = cv2.split(img_arr)
    #print(len(chans), ' -> ', [len(chan) for chan in chans])

    colors = ("b", "g", "r")
    plt.title("Title")
    plt.xlabel("labelx")
    plt.ylabel("ylabel")

    try:
        for (chan, color) in zip(chans, colors):
            hist = cv2.calcHist([chan], [0], None, [256], [0,256])
            plt.plot(hist, color = color)
            plt.xlim([0,256])
            # plt.savefig("D://careers//python-my-projects//django//project-code//django_project//server2//django_project//servAgri//output//histo_out//" + index + "-histo.png")
            #print('ok ' + chan +  color)
        #plt.show()
        # new_image_path
        plt.savefig("D://careers//python-my-projects//django//project-code//django_project//server2//django_project//servAgri//output//histo_out//" + index + "-histo.png")
        return 'now ok'
    except:
        print('not ok')
        
    """
        from PIL import Image
        img = Image.open(self.image.path)
        if(img.width > 300 or img.height > 300):
            image_size = (300, 300)
            img.thumbnail(image_size)
            img.save(self.image.path)
    """