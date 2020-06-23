import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

def graphtextdetector(img):
    
    custom_config=r'--oem 3 --psm 6'

    text=pytesseract.image_to_string(img,config=custom_config)
    data1=[]
    for j in text.split('\n'):
        data1.append(j.split(' '))
    # ranges=[]

    i=len(data1)-1
    while i>=0:
        count=0
        for val in data1[i]:
            if val.isdigit():
                count+=1
        if count>=3:
            break

        i-=1
    
    elements=[]

    for j in data1[i]:
        if j.isdigit():
            elements.append(int(j))

    diff=[]
    for j in range(len(elements)-1):
        if elements[j+1]-elements[j]>0:
            diff.append(elements[j+1]-elements[j])

    freq={}
    for i in diff:
        freq[i]=diff.count(i)    

    max=0
    maxnumber=0

    for key,value in freq.items():
        if value>max:
            max=value
            maxnumber=key

    return maxnumber

    # return data1[i]

if __name__ == "__main__":
    image_path='case3.png'
    image_path='mixed.jpg'
    img=cv2.imread(image_path)
    d=graphtextdetector(img)
    print(d)
