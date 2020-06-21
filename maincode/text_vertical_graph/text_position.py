import pytesseract
from pytesseract import pytesseract
import cv2
import matplotlib.pyplot as plt


##remove special characters

def barlabelandheightratio(img,xaxismaximum=0,yaxismaximum=0):

    y=img.shape[0]-yaxismaximum
    h,w=img.shape[:2]

    custom_config=r'--oem 3 --psm 6'
    data=pytesseract.image_to_boxes(img,config=custom_config)
    matrix=data.split("\n")
    l=[]
    label=""
    bar_labels=[]
    bar_positions=[]
    i=0
    flag=0

    for j in matrix:
        l.append(j.split(" "))

    while i<(len(l)-1):

        xaverage1=((int(l[i][1])+int(l[i][3]))/2)
        xaverage2=((int(l[i+1][1])+int(l[i+1][3]))/2)

        yaverage1=((int(l[i][2])+int(l[i][4]))/2)
        yaverage2=((int(l[i+1][2])+int(l[i+1][4]))/2)

        if xaverage1>xaxismaximum:
            
            label=""
            while xaverage1>x and i<len(l)-1:
                i+=1
                xaverage1=((int(l[i][1])+int(l[i][3]))/2)

            flag=0
            continue
        
        ###write condition for labels with length one
        

        if abs(yaverage2-yaverage1)<=15 and abs(xaverage2-xaverage1)<50:
            flag=1
            if abs(xaverage2-xaverage1)<30:
                label+=l[i][0]
            else:
                label+=l[i][0]
                label+=" "

        if ((abs(xaverage2-xaverage1)>40 and xaverage2<xaxismaximum) or (abs(xaverage2-xaverage1)<40 and xaverage2>xaxismaximum)) and abs(yaverage2-yaverage1)<15:
            label=""
            flag=0
        elif xaverage2>xaxismaximum or abs(yaverage2-yaverage1)>15 and abs(xaverage2-xaverage1)>30:
            if flag==1:
                label+=l[i][0]
                bar_labels.append(label)
                label=""
                bar_positions.append(h-(int(l[i-1][2])+int(l[i-1][4]))/2)
            else:
                if xaverage1>(xaxismaximum)*(1/3) and l[i][0] not in ['.','@','\'','`','!','-']:
                    bar_labels.append(l[i][0])
                    bar_positions.append(h-yaverage1)

            flag=0


        i+=1

    print(bar_labels,bar_positions)
     #####calculate ranges and height/pixel ratio


    # for i in l:
    #     print(i)


if __name__ == "__main__":
    img_path='case2.png'
    img=cv2.imread(img_path)
    x=113
    y=562
    barlabelandheightratio(img,x,y)

    # print(d)
    plt.imshow(img)
    plt.show()