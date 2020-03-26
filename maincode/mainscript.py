import cv2
import bar_extracter
import heightcalculator
import extracted_data
import textposition


def mainfunction(img_path):
    img=cv2.imread(img_path)
    img_gray=cv2.imread(img_path,0)

    ed=extracted_data.extractdata(img_path)

    rangeratio=ed[1]
    data=ed[0]

    only_bars=bar_extracter.obtainbars(img_gray)

    hei=heightcalculator.heightcalculation(only_bars)
    ##########
    yaxisminimum=hei[0]
    heights=hei[1]
    barlocation1=hei[2]

    tpos=textposition.barlabelandheightratio(img,yaxisminimum)
    heightratio=tpos[0]
    bartitle=tpos[1]
    barlocation2=tpos[2]

    data['datatitles']=bartitle

    ##############
    # print(barlocation2)
    # print(barlocation1)

    newheights=[]
    if len(barlocation1)!=len(barlocation2):
        j=0
        barlocation1.append(img.shape[1])
        for i in range(len(barlocation2)):
            if abs(barlocation1[j]-barlocation2[i])>30:
                newheights.append(0)
            else:
                newheights.append(heights[j])
                j=j+1
            
        heights=newheights

    bar_readings=[]

    for i in range(len(heights)):
        readingofabar=rangeratio*heights[i]//heightratio
        bar_readings.append(readingofabar)

    print(data['datatitles'])
    
    print(bar_readings)
    # print(barlocation2)
    # print(barlocation1)

if __name__=="__main__":
    img_path="raghav.png"
    mainfunction(img_path)