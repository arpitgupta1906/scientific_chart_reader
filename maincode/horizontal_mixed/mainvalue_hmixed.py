import cv2
import os, sys
import matplotlib.pyplot as plt
from math import ceil
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from horizontal_mixed import filterimage
from horizontal_mixed import height_calculator
from text_vertical_graph import text_position

def mainfunction(img_path):
    img=cv2.imread(img_path)
    img_gray=cv2.imread(img_path,0)

    only_bars=filterimage.obtainbars(img_gray)
    (yaxismaximum,xaxismaximum,heights,bar_position,diff)=height_calculator.heightcalculator(only_bars)
    (ratio,bartitle,barlocation2)=text_position.barlabelandheightratio(img,xaxismaximum,yaxismaximum)

    data={}
    data['datatitles']=bartitle
    
    i=0
    j=0
    main_heights=[]

    while i<len(heights) and j<len(bartitle):
        d=bar_position[i][0]

        l=[]
        if abs(barlocation2[j]-(d+bar_position[i][1])/2)<35:
            l.append(heights[i])
            i+=1
            while i<len(heights) and abs(barlocation2[j]-(d+bar_position[i][1])/2)<30:
                l.append(heights[i])
                i+=1

            main_heights.append(l)
            j+=1

        else:
            j+=1
            main_heights.append([0])

    while j<len(bartitle):
        j+=1
        main_heights.append([0])

    ###############
    final_heights=[]
    mx=0
    count=0
    for bar in main_heights:
        if bar[0]==0:
            final_heights.append(bar)
            continue
        temp=[]
        inside=1
        temp.append(bar[0])
        count+=1
        prev=bar_position[count-1][1]
        while inside<len(bar):
            if abs(prev-bar_position[count][0])<5:
                temp.append(bar[inside])
                prev=bar_position[count][1]
                inside+=1
                count+=1
            elif prev-bar_position[count-1][1]<=diff+4:
                temp.append(0)
                prev=prev+diff

        mx=max(len(temp),mx)
        final_heights.append(temp)


    for bar in final_heights:
        r=mx-len(bar)
        for _ in range(r):
            bar.append(0)

    bar_readings=[]
    maxreading=0
    for bar in final_heights:
        temp=[]
        for var in bar:
            readingofabar=ceil(var*ratio)
            maxreading=max(maxreading,readingofabar)
            temp.append(readingofabar)
        bar_readings.append(temp)


    # print(bar_readings)
    # print('----------------')
    # print(data['datatitles'])

    return [data['datatitles'],bar_readings]



if __name__ == "__main__":
    img_path="please.png"
    print(mainfunction(img_path))