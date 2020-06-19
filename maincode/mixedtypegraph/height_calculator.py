import cv2
import matplotlib.pyplot as plt
import numpy as np
# from statistics import mode 


# background_color=255

def xaxiscoordinate(image):
    
    h,w=image.shape

    # l=[image[10,10],image[20,40],image[h-20,20]]
    # background_color=mode(l)

    flag=0
    for y in range(h-1,0,-1):
        for x in range(0,w*2//3,5):
            flag=1
            for i in range(5):
                if image[y,x+i]==255:
                    flag=0
                    break
            if flag==1:
                return [y,x] 


def heightcalculator(image):

    h,w=image.shape

    xy,xx=xaxiscoordinate(image)

if __name__ == "__main__":
    image_path="test_filtered.png"
    image=cv2.imread(image_path,0)
    print(xaxiscoordinate(image))