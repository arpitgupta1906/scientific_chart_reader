import cv2
import filterimage
import height_calculator
import os, sys
import matplotlib.pyplot as plt
from math import ceil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from text_vertical_graph import text_position

def mainfunction(img_path):
    img=cv2.imread(img_path)
    img_gray=cv2.imread(img_path,0)

    only_bars=filterimage.obtainbars(img_gray)
    (yaxismaximum,xaxismaximum,heights,bar_position)=height_calculator.heightcalculation(only_bars)
    (ratio,bartitle,barlocation2)=text_position.barlabelandheightratio(img,xaxismaximum,yaxismaximum)


    data={}
    data['datatitles']=bartitle
    mx_index=0

    for i in range(1,len(heights)):
        if len(heights[i])>len(heights[mx_index]):
            mx_index=i

    mx=len(heights[mx_index])

    colors=[]

    for i in heights[mx_index]:
        colors.append(i[0])

    j=0
    new_heights=[]

    for i in range(len(barlocation2)):
        if abs(barlocation2[i]-bar_position[j])<30:
            if len(heights[j])<mx:
                temp=[]

                pos=0

                for k in range(mx):
                    if abs(heights[j][pos][0]-colors[k])<10:
                        temp.append(heights[j][pos][1])
                    else:
                        temp.append(0)
                new_heights.append(temp)

            else:
                temp=[]
                for bar in heights[j]:
                    temp.append(bar[1])

                new_heights.append(temp)

            j+=1
        else:
            temp=[]
            for h in range(mx):
                temp.append(0)
            new_heights.append(temp)

    bar_readings=[]

    for bar in new_heights:
        temp=[]
        for i in bar:
            readingofabar=ceil(i*ratio)
            temp.append(readingofabar)
        
        bar_readings.append(temp)

    # print('----------------')
    # print(bar_readings)
    # print('----------------')
    # print(data)

    return [data['datatitles'],bar_readings]

if __name__ == "__main__":
    img_path="case3.png"
    print(mainfunction(img_path))