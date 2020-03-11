import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv
import matplotlib.pyplot as plt

img = 'test.png'
imge=cv2.imread(img)
data=pytesseract.image_to_boxes(imge)
print(data)
#a=data[5:9]
#b=data[6:9]
#print(b)
#c=a-b
#print(c)
d=len(data)
#print(d)



#plt.imshow(imge)
#plt.show()
