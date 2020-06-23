import cv2
import numpy as np
import matplotlib.pyplot as plt


def obtainbars(img):
    """
    Pass a gray scaled image as input to obtain only the bars
    """



    # Thresholding the image
    (thresh, img_bin) = cv2.threshold(img, 240, 255,0)
    # Invert the image
    img_bin = 255-img_bin 

    # Defining a kernel length
    kernel_length = np.array(img).shape[1]//80
    
    # A horizontal kernel of (kernel_length X 1), which will help to detect all the horizontal line from the image.
    hori_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_length, 10))

    # A kernel of (3 X 3) ones.
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))


    # Morphological operation to detect horizontal lines from an image
    img_temp2 = cv2.erode(img_bin, hori_kernel, iterations=3)
    horizontal_lines_img = cv2.dilate(img_temp2, hori_kernel, iterations=3)
    horizontal_lines_img = 255-horizontal_lines_img

    return horizontal_lines_img
    
if __name__=="__main__":
    # Read the image
    # img = cv2.imread('1.png', 0)
    img=cv2.imread('test.png',0)
    horizontal_lines_img=obtainbars(img)
    # cv2.imwrite("test.png",horizontal_lines_img)
    plt.imshow(horizontal_lines_img,cmap="gray")
    plt.show()

