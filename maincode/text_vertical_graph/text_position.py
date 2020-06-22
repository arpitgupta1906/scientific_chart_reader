import pytesseract
from pytesseract import pytesseract
import cv2
import matplotlib.pyplot as plt


##remove special characters
##yaxismax=last y coordinate of the bar
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
            while xaverage1>xaxismaximum and i<len(l)-1:
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
        elif (xaverage2>xaxismaximum and abs(yaverage2-yaverage1)>15) and abs(xaverage2-xaverage1)>30:
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
        elif (xaverage2>xaxismaximum or abs(yaverage2-yaverage1)>15):
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

     #####calculate ranges and height/pixel ratio
    print(bar_labels)
    pos=0
    while pos<len(l) and (int(l[pos][3])<xaxismaximum or int(l[pos][4])>=y):
        pos+=1


    bar_readings=[]
    bar_diff=[]
    initial=img.shape[1]

    while pos<len(l)-1 and int(l[pos][3])>=xaxismaximum:

        while pos<len(l)-1 and (not l[pos][0].isdigit()):
            pos+=1 

        if pos>=len(l)-1:
            break
        temp=""
        xaverage1=((int(l[pos][1])+int(l[pos][3]))/2)
        xaverage2=((int(l[pos+1][1])+int(l[pos+1][3]))/2)

        yaverage1=((int(l[pos][2])+int(l[pos][4]))/2)
        yaverage2=((int(l[pos+1][2])+int(l[pos+1][4]))/2)
        
        xpos1=xaverage1
        xpos2=0

        while pos<len(l)-1 and (l[pos][0].isdigit() and abs(yaverage2-yaverage1)<10 and abs(xaverage1-xaverage2)<30):
            temp+=l[pos][0]
            
            pos+=1
            initial=yaverage1
            if pos>=len(l)-1:
                break 

            xaverage1=((int(l[pos][1])+int(l[pos][3]))/2)
            xaverage2=((int(l[pos+1][1])+int(l[pos+1][3]))/2)

            yaverage1=((int(l[pos][2])+int(l[pos][4]))/2)
            yaverage2=((int(l[pos+1][2])+int(l[pos+1][4]))/2)

            xpos2=xaverage1


        if l[pos][0].isdigit():
            temp+=l[pos][0]
        if len(temp)>0:
            if len(temp)>1:
                bar_diff.append(abs(xpos1+xpos2)/2)
            else:
                bar_diff.append(abs(xpos1))
            bar_readings.append(int(temp))
        
        pos+=1

    print(bar_readings)
    # for i in matrix:
    #     print(i)
    # print(bar_labels,bar_positions)
    # print(bar_diff,bar_readings)
    
    diff_xaxis=[]
    bar_diff.sort()
    for d in range(len(bar_diff)-1):
        if bar_diff[d+1]-bar_diff[d]>0:
            diff_xaxis.append(bar_diff[d+1]-bar_diff[d])

    diff_xaxis.sort()
    k=len(diff_xaxis)
    
    height_ratio=diff_xaxis[k//2]

    diff=[]

    for m in range(len(bar_readings)-1):
        diff.append(bar_readings[m+1]-bar_readings[m])

    freq={}
    for m in diff:
        freq[m]=diff.count(m)

    max=0
    maxnumber=0

    for key,value in freq.items():
        if value>max:
            max=value 
            maxnumber=key

    ratio=maxnumber/height_ratio

    # print(maxnumber)
    mark=0
    initial=img.shape[0]-initial

    # while mark<len(bar_positions) and bar_positions[mark]<initial-10:
    while mark<len(bar_positions) and bar_positions[mark]<yaxismaximum:
        mark+=1
    
    return [ratio,bar_labels[:mark],bar_positions[:mark]]

if __name__ == "__main__":
    img_path='case2.png'
    img=cv2.imread(img_path)
    x=113
    y=562
    plt.imshow(img)
    plt.show()
    print(barlabelandheightratio(img,x,y))

    # print(d)