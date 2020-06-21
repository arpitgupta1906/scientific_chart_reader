import cv2
import matplotlib.pyplot as plt
import numpy as np

BACKGROUND_COLOR=255

def axiscoordinate(image):
    h,w=image.shape[:2]
    flag=0

    for x in range(0,w*2//3,5):
        for y in range(h-10):
            flag=1
            for i in range(3):
                if image[y,x+i]==BACKGROUND_COLOR:
                    flag=0
                    break
            if flag==1:
                return [y,x]


def heightcalculation(image):
    h,w=image.shape
    xy,xx=axiscoordinate(image)

    y=yinitial=xy 
    x=xinitial=xx
    height=[]
    barlocation=[]
    x+=2
    yend=xy

    while y<h-30:

        while image[y,x]==BACKGROUND_COLOR and image[y+1,x]==BACKGROUND_COLOR and y<h-30:
            y+=1

        flag=0
        xinitial=x
        yinitial=y+2
        y+=2

        while image[y,x]!=BACKGROUND_COLOR and y<h-30:
            y+=1

        xmid=x
        ymid=(yinitial+(y-2))//2
        color=int(image[ymid,xmid])
        

        temp=[]
        while image[ymid,xmid]!=BACKGROUND_COLOR and xmid<w-30:
            while abs(int(image[ymid,xmid])-color)<9 and xmid<w-30:
                xmid+=1

            flag=1

            temp.append([color,abs(xmid-xinitial)])
            xinitial=xmid
            xmid+=4   ######
            color=int(image[ymid,xmid])

        if flag==1:
            yend=y
            height.append(temp)
            barlocation.append(ymid)


    return [yend,xx,height,barlocation]


if __name__ == "__main__":
    image_path="test_filtered.png"
    image=cv2.imread(image_path,0)
    print(axiscoordinate(image))
    print(heightcalculation(image))
    plt.imshow(image,cmap="gray")
    plt.show()