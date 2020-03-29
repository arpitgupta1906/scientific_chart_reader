import pytesseract
from pytesseract import pytesseract
import cv2
import matplotlib.pyplot as plt


def barlabelandheightratio(img,yaxisminimum=0):
    """
    This function returns the ratio of the range,
    the x axis labels and the postiton of the bars
    """

    
    y=img.shape[0]-yaxisminimum


    custom_config=r'--oem 3 --psm 6'
    data=pytesseract.image_to_boxes(img,config=custom_config)
    l=data.split("\n")
    matrix=[]

    for i in l:
        matrix.append(i.split(" "))
        # matrix[i][2]=(int(matrix[i][2])-img.shape[0])
        # matrix[i][4]=(int(matrix[i][4])-img.shape[0])

    numberlist=[]


    for i in matrix:

        ###############
        if i[0].isdigit() and int(i[2])>y-10:
            # print(i)
            numberlist.append((int(i[2])+int(i[4]))/2)


    unit_data=[]

    for i in range(1,len(numberlist)):
        d=abs(numberlist[i]-numberlist[i-1])
        if d>7:
            unit_data.append(d)


    unit_data.sort()
    k=len(unit_data)
    height_ratio=unit_data[k//2]
    # print(data)


    bartitleposition=[]
    bartitle=[]

    labelbegin=0

# return the beginning coordinates of the labels 
    for i in range(len(matrix)):
        if int(matrix[i][4])<y:
            labelbegin=i 
            break 


    s="" 
    flagnext=0
    j=0

    for i in range(labelbegin,len(matrix)-1):
        yaverage=(int(matrix[i][2])+int(matrix[i][4]))/2
        xaverage=(int(matrix[i][1])+int(matrix[i][3]))/2

        yaverage2=(int(matrix[i+1][2])+int(matrix[i+1][4]))/2
        xaverage2=(int(matrix[i+1][1])+int(matrix[i+1][3]))/2
        
        if abs(yaverage-yaverage2)<=10 and abs(xaverage-xaverage2)<=30:
            j=xaverage
            break 
    ############
    maxlength=img.shape[1]
    maxheight=img.shape[0]
    matrix.append(['_',str(maxlength),str(maxheight),str(maxlength),str(maxheight)])
    #code that returns the bar positions
    for i in range(labelbegin,len(matrix)-1):
        yaverage=(int(matrix[i][2])+int(matrix[i][4]))/2
        xaverage=(int(matrix[i][1])+int(matrix[i][3]))/2

        yaverage2=(int(matrix[i+1][2])+int(matrix[i+1][4]))/2
        xaverage2=(int(matrix[i+1][1])+int(matrix[i+1][3]))/2
        
        if abs(yaverage-yaverage2)<=10:
            if abs(xaverage-xaverage2)<=30:
                s=s+matrix[i][0]
                if flagnext==1:
                    j=xaverage
                    flagnext=0
            else: 
                s=s+matrix[i][0]
                bartitle.append(s)
                if len(s)==1:
                    bartitleposition.append(xaverage)
                else:
                    bartitleposition.append(abs(xaverage+j)/2)
                flagnext=1
                s=""

        else:
            s=s+matrix[i][0]
            diff=((int(matrix[i][1])+int(matrix[i][3]))/2)
            #if the label is one letter then directly add the coordinate
            if len(s)==1:
                bartitleposition.append(diff)
            else:
                bartitleposition.append((diff+j)/2)
            bartitle.append(s)
            break  

    # print(unit_data)
    # print(height_ratio)
    # print(bartitle)
    # print(bartitleposition)

    return [height_ratio,bartitle,bartitleposition]
    

if __name__=="__main__":
    img_path = 'image4.png'
    img=cv2.imread(img_path)
    yaxisminimum=554
    d=barlabelandheightratio(img,yaxisminimum)
    print(d)
    plt.imshow(img)
    plt.show()