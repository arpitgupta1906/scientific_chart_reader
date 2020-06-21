import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt

def graphtextdetector(image_path):
    img=cv2.imread(image_path)
    custom_config=r'--oem 3 --psm 6'

    text=pytesseract.image_to_string(img,config=custom_config)

    return text

if __name__ == "__main__":
    image_path='case3.png'
    d=graphtextdetector(image_path)
    print(d)
