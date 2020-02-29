import cv2
import matplotlib.pyplot as plt

image_path="image5.png"

image=cv2.imread(image_path)
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# cv2.imshow("grayscale",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def blur(image):
    return cv2.GaussianBlur(image,(5,5),0)

# def thresholding(image):
#     # image=blur(image)
#     return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# image=thresholding(image)
# image=blur(image)

h,w=image.shape


# some=0
# flag=0
# for i in range(h):
#     for j in range(w):
#         if image[i,j]==0:
#             print(str(i)+" "+str(j))
#             some =some+1
#         if some==10:
#             flag=1
#             break
#     if flag==1:
#         break




def threshold(T,image):
    h,w=image.shape

    for y in range(h):
        for x in range(w):
            image[y,x]=255 if image[y,x]>=T else 0

    return image

image=threshold(250,image)

def xaxiscoordinate(image):
    h,w=image.shape
    flag=0
    for y in range(h-1,0,-1):
        for x in range(w*2//3):
            flag=1
            for i in range(80):
                if image[y,x+i]!=0:
                    flag=0
                    break
            if flag==1:
                # y=y-40
                # j=0
                # while image[y,x]==0:
                #     x=x+1
                
                # while image[y,x]==255:
                #     y=y-1

                return [y-1,x] 

#implement a checker to verify line starting from between

print(xaxiscoordinate(image))

plt.imshow(image,cmap="gray")
plt.show()
