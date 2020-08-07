import cv2
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import matplotlib.pyplot as plt

from vertical_mixed import filterimage
from vertical_mixed import height_calculator
import extracted_data
import textposition


def mainfunction(img_path):

    img=cv2.imread(img_path)
    img_gray=cv2.imread(img_path,0)

    (data,rangeratio)=extracted_data.extractdata(img_path)

    only_bars=filterimage.obtainbars(img_gray)

    (yaxisminimum,heights,bar_position,diff)=height_calculator.heightcalculator(only_bars)
    
    (heightratio,bartitle,barlocation2)=textposition.barlabelandheightratio(img,yaxisminimum)
    i=0
    j=0
    main_heights=[]

    data['datatitles']=bartitle

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

        # check for zeros by checking l and removing extras by decreasing values of i

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
            readingofabar=rangeratio*var//heightratio
            maxreading=max(maxreading,readingofabar)
            temp.append(readingofabar)
        bar_readings.append(temp)

    if maxreading>data['Yaxis_plotdata'][0]+30:
        bar_readings=[]
        heightratio*=2

        for bar in final_heights:
            temp=[]
            for var in bar:
                readingofabar=rangeratio*var//heightratio
                temp.append(readingofabar)
            bar_readings.append(temp)

    # print(bar_readings)
    # print('-----------------')
    # print(final_heights)
    # print('-----------------')
    # print([data,rangeratio])
    # print('-----------------')
    # print(heightratio)
    # print('-----------------')
    # print(heights)
    # print('-----------------')
    # print([bartitle,barlocation2])

    # plt.imshow(img)
    # plt.show()

    return [data['datatitles'],bar_readings]

if __name__ == "__main__":
    img_path='image2.png'
    print(mainfunction(img_path))