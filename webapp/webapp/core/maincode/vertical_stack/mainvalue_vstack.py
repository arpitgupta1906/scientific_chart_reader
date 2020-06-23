import cv2
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matplotlib.pyplot as plt

from vertical_stack import filterimage
from vertical_stack import height_calculator
import extracted_data
import textposition

def mainfunction(img_path):
    img=cv2.imread(img_path)
    img_gray=cv2.imread(img_path,0)

    (data,rangeratio)=extracted_data.extractdata(img_path)

    only_bars=filterimage.obtainbars(img_gray)
    (yaxisminimum,heights,bar_position)=height_calculator.heightcalculation(only_bars)

    (heightratio,bartitle,barlocation2)=textposition.barlabelandheightratio(img,yaxisminimum)

    mx_index=0
    data['datatitles']=bartitle
    
    for i in range(1,len(heights)):
        if len(heights[i])>len(heights[mx_index]):
            mx_index=i

    mx=len(heights[mx_index])

    colors=[]

    for i in heights[mx_index]:
        colors.append(i[0])

    j=0
    new_heights=[]
    # print(heights)
    for i in range(len(barlocation2)):
        if(abs(barlocation2[i]-bar_position[j])<30):
            if len(heights[j])<mx:
                temp=[]

                pos=0
                
                for k in range(mx):
                    if pos<len(heights[j]) and abs(heights[j][pos][0]-colors[k])<10:
                        temp.append(heights[j][pos][1])
                        pos+=1
                        
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
            readingofabar=rangeratio*i//heightratio
            temp.append(readingofabar)
        
        bar_readings.append(temp)


    # print('------------')
    # print(bar_readings)
    # print('------------')
    # print(data)

    return [data['datatitles'],bar_readings]
if __name__ == "__main__":
    # img_path="stack3.png"
    img_path="please.png"
    mainfunction(img_path)