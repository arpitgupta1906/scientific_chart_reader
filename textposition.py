import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv

img = 'test.png'
imge = Image.open(img)
data=pytesseract.image_to_boxes(imge)

print(data)