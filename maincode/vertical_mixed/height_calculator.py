import cv2
import matplotlib.pyplot as plt
import numpy as np
from statistics import median
from math import ceil

# background_color=255

def xaxiscoordinate(image):
    
    h,w=image.shape

    flag=0
    for y in range(h-1,0,-1):
        for x in range(0,w*2//3,5):
            flag=1
            for i in range(5):
                if image[y,x+i]!=0:
                    flag=0
                    break
            if flag==1:
                return [y,x] 


def heightcalculator(image):

    h,w=image.shape

    xy,xx=xaxiscoordinate(image)

    y=yinitial=xy 
    x=xinitial=(xx+3)
    bar_coordinates=[]
    bar_heights=[]

    while x<w-25:

        while image[y,x]!=0 and x<w-10:
            x+=1

        xinitial=x

        flag=0
        
        while image[y,x]==0 and y>30:
            y-=1
            flag=1
        
        y+=5

        while flag==1 and image[y,x]==0 and image[y-10,x]!=0 and image[y+10,x]==0 and x<w-10:
            x+=1 

        if flag==1:
            bar_heights.append(yinitial-y+5)
            bar_coordinates.append([xinitial,x])
            xinitial=x
            y=yinitial

    diff=[]
    for bar in bar_coordinates:
        diff.append(ceil(bar[1]-bar[0]))
    
    diff.sort()
    width=median(diff)

    return [xy,bar_heights,bar_coordinates,width]

if __name__ == "__main__":
    image_path="test_filtered.png"
    image=cv2.imread(image_path,0)
    print(heightcalculator(image))