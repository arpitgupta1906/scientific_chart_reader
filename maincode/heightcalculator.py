import cv2
import matplotlib.pyplot as plt
import numpy as np

def blur(image):
    return cv2.GaussianBlur(image,(5,5),0)

# def thresholding(image):
#     # image=blur(image)
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# def threshold(T,image):
#     h,w=image.shape

#     for y in range(h):
#         for x in range(w):
#             image[y,x]=255 if image[y,x]>=T else 0

#     return image

def xaxiscoordinate(image):
    h,w=image.shape
    flag=0
    for y in range(h-1,0,-1):
        for x in range(0,w*2//3,5):
            flag=1
            for i in range(5):
                if image[y,x+i]!=0:
                    flag=0
                    break
            if flag==1:
                return [y,x] 


def heightcalculation(image):
    """
    This function returns yaxisminimum,bar height,and the positions of
    the bars.
    """
    h,w=image.shape
    xy,xx=xaxiscoordinate(image)
    # print([xy,xx])
    
    # plt.imshow(image,cmap="gray")
    # plt.show()
    y=yiniial=xy
    x=xx
    heightpixellist=[]
    barlocation=[]

    while x<w-10:
        while image[y,x]==255 and x<w-10:
            x=x+1
        
        flag=0
        while image[y,x]==0 and y>10:
            flag=1
            y=y-1

        if flag==1:
            heightpixellist.append(yiniial-y)
            y=yiniial

        xi=x

        while image[y,x]==0 and x<w-10:
            x=x+1

        # if flag==1:
        barlocation.append((x+xi)/2)

    return [xy,heightpixellist,barlocation[:len(barlocation)-1]]


#####Unused#####
def iterate_regions(image):
    h, w = image.shape

    for i in range(h - 15):
      for j in range(w - 15):
        im_region = image[i:(i + 16), j:(j + 16)]
        yield im_region, i, j

#####Unused#####
def filtered_image(image):
    h,w=image.shape

    op=np.zeros((h-15,w-15))
    
    for im_region,i,j in iterate_regions(image):
        flag=0
        a,b=im_region.shape
        for y in range(a):
            for x in range(b):
                if y==0 or y==a-1 or x==0 or x==b-1:
                    if im_region[y,x]>0:
                        flag=1
                        break 
            if flag==1:
                break 
        
        if flag==1:
            op[i,j]=255
        else :
            op[i,j]=0
    
    return op


def initialcall():

    image_path="1.png"

    image=cv2.imread(image_path,0)
    
    # image=cv2.medianBlur(image,5)
    # image=thresholding(image)

    image=threshold(250,image)
    image=filtered_image(image)

    #implement a checker to verify line starting from between
    # print(xaxiscoordinate(image))
    plt.axis("off")
    plt.imshow(image,cmap="gray")

    plt.savefig("1_filtered.png")
    plt.show()


if "__main__"==__name__:
    image_path="test.png"
    image=cv2.imread(image_path,0)
    print(heightcalculation(image))
    # initialcall()