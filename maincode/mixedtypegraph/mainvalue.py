import cv2
import filterimage
import height_calculator
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

    while i<len(heights) and j<len(bartitle):
        d=bar_position[i][0]

        l=[]
        if abs(barlocation2[j]-(d+bar_position[i][1])/2)<30:
            l.append(heights[i])
            i+=1
            while i<len(heights) and abs(barlocation2[j]-(d+bar_position[i][1])/2)<30:
                l.append(heights[i])
                i+=1

        # check for zeros by checking l and removing extras by decreasing values of i
           
            main_heights.append(l)
            j+=1

        else:
            j+=1
            main_heights.append([0])

    print(main_heights)
    print('-----------------')
    print([data,rangeratio])
    print('-----------------')
    print(bar_position)
    print('-----------------')
    print(heights)
    print('-----------------')
    print([bartitle,barlocation2])

if __name__ == "__main__":
    img_path='image2.png'
    mainfunction(img_path)