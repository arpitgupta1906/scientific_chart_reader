import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv

img_path = 'image2.png'
# img = Image.open(img)
# data=pytesseract.image_to_boxes(imge)

custom_config_number=r'--oem 3 --psm 6 outputbase digits'
custom_config=r'--oem 3 --psm 6'

# custom_config1=r'--oem 3 --psm 1'

# custom_config2=r'--oem 3 --psm 4'
img=cv2.imread(img_path)
data=pytesseract.image_to_boxes(img,config=custom_config)
# print(data)
l=data.split("\n")
matrix=[]

for i in l:
    matrix.append(i.split(" "))

numberlist=[]

for i in matrix:
    if i[0].isdigit():
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
print(data)
print(unit_data)
print(height_ratio)
# print(matrix)

