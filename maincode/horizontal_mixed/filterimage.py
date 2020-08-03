import cv2
import numpy as np
import matplotlib.pyplot as plt
# from sklearn.cluster import MiniBatchKMeans

def obtainbars(img):
    """
    Pass a gray scaled image as input to obtain only the bars
    """



    # Thresholding the image
    (thresh, img_bin) = cv2.threshold(img, 240, 255,0)
    # Invert the image
    
    # img_bin=img
    # img_bin=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    img_bin = 255-img_bin 

    # plt.imshow(img)
    # plt.show()

    # Defining a kernel length
    kernel_length = np.array(img).shape[1]//100
    
    # A vertical kernel of (1 X kernel_length), which will help to detect all the vertical line from the image.
    verticle_kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,kernel_length))


    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Morphological operation to detect vertical lines from an image
    
    img_temp1=cv2.erode(img_bin,verticle_kernel,iterations=3)
    verticle_lines_img=cv2.dilate(img_temp1,verticle_kernel,iterations=3)
    verticle_lines_img=255-verticle_lines_img

    return verticle_lines_img

    
if __name__=="__main__":
    # Read the image
    # img = cv2.imread('case3.png', 0)
    img=cv2.imread('mixed.jpg',0)
    horizontal_lines_img=obtainbars(img)
    cv2.imwrite("test_filtered.png",horizontal_lines_img)
    plt.imshow(horizontal_lines_img,cmap="gray")
    plt.show()

