import cv2
import numpy as np

img = cv2.imread('test.png', 0)

ret,img = cv2.threshold(img, 200, 255, 0)
cv2.imshow('Input', img)
kernel = np.ones((2,2), np.uint8)

img = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)


cv2.imshow('Erosion', img)
cv2.imshow('Dilation', img_dilation)


#SKELETONIZATION

cv2.waitKey(0)

size = np.size(img)
skel = np.zeros(img.shape, np.uint8)

# Get a Cross Shaped Kernel
element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))


# Repeat steps 2-4
while True:
    #Step 2: Open the image
    open = cv2.morphologyEx(img, cv2.MORPH_OPEN, element)
    #Step 3: Substract open from the original image
    temp = cv2.subtract(img, open)
    #Step 4: Erode the original image and refine the skeleton
    eroded = cv2.erode(img, element)
    skel = cv2.bitwise_or(skel,temp)
    img = eroded.copy()
    # Step 5: If there are no white pixels left ie.. the image has been completely eroded, quit the loop
    if cv2.countNonZero(img)==0:
        break

# Displaying the final skeleton
cv2.imshow("Skeleton",skel)
#cv2.imwrite('skeletonoftest.png',skel)
cv2.waitKey(0)
cv2.destroyAllWindows()