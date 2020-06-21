import cv2
import matplotlib.pyplot as plt
import numpy as np
from statistics import median
from math import ceil

def axiscoordinate(image):
    h,w=image.shape[:2]
    flag=0

    for x in range(0,w*2//3,5):
        for y in range(h-10):
            flag=1
            for i in range(3):
                if image[y,x+i]==255:
                    flag=0
                    break
            if flag==1:
                return [y,x]

def heightcalculator(image):

    h,w=image.shape[:2]

    xy,xx=axiscoordinate(image)

    y=yinitial=xy 
    x=xinitial=xx
    bar_coordinates=[]
    bar_heights=[]
    initial_pos=0

    while y<h-20:
        while image[y,x]!=0 and y<h-20:
            y+=1

        yinitial=y
        flag=0

        while image[y,x]==0 and x<w-30:
            x+=1
            flag=1

        x-=2

        while flag==1 and image[y,x]==0 and image[y,x+4]!=0 and image[y,x-4]==0 and y<h-20:
            y+=1

        if flag==1:
            bar_heights.append(abs(xinitial-(x+2)))
            bar_coordinates.append([yinitial,y])
            x=xinitial
            yinitial=y
            initial_pos=y

    diff=[]
    for bar in bar_coordinates:
        diff.append(ceil(bar[1]-bar[0]))

    diff.sort()
    width=median(diff)

    return [initial_pos,xx,bar_heights,bar_coordinates,width]


if __name__ == "__main__":
    image_path="test_filtered.png"
    image=cv2.imread(image_path,0)
    # print(axiscoordinate(image))
    plt.imshow(image,cmap="gray")
    plt.show()
    print(heightcalculator(image))