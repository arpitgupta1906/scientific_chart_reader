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
plt.imshow(imge,cmap="gray")
plt.show()
