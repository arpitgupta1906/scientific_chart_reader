import cv2
import matplotlib.pyplot as plt
import numpy as np

BACKGROUND_COLOR=255

def xaxiscoordinate(image):
    h,w=image.shape
    flag=0


    for y in range(h-1,0,-1):
        for x in range(0,w*2//3,5):
            flag=1
            for i in range(5):
                if image[y,x+i]==BACKGROUND_COLOR:
                    flag=0
                    break
            if flag==1:
                return [y,x] 


def heightcalculation(image):
    h,w=image.shape
    xy,xx=xaxiscoordinate(image)

    y=yinitial=xy
    x=xinitial=xx
    height=[]
    barlocation=[]
    y-=2

    while x<w-10:
        
        while image[y,x]==BACKGROUND_COLOR and image[y,x+1]==BACKGROUND_COLOR and x<w-10:
            x+=1
        
        flag=0
        xinitial=x+2
        yinitial=y
        x+=2
        

        while image[y,x]!=BACKGROUND_COLOR and x<w-10:
            x+=1

        xmid=(xinitial+(x-2))//2
        ymid=y
        color=int(image[ymid,xmid])

        # print(image[ymid,xmid])
        temp=[]
        while image[ymid,xmid]!=BACKGROUND_COLOR and ymid>30:
            while abs(int(image[ymid,xmid])-color)<9 and ymid>30:
                ymid-=1

            flag=1
            
            temp.append([color,abs(ymid-yinitial)])
            yinitial=ymid
            ymid-=4
            color=int(image[ymid,xmid])
        
        if flag==1:
            height.append(temp)
            barlocation.append(xmid)
        

    return [xy,height,barlocation]


if __name__ == "__main__":
    image_path="test.png"
    image=cv2.imread(image_path,0)
    print(heightcalculation(image)[1])
    plt.imshow(image,cmap="gray")
    plt.show()