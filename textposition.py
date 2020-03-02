import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv

img_path = 'test.png'
# img = Image.open(img)
# data=pytesseract.image_to_boxes(imge)

# custom_config_number=r'--oem 3 --psm 6 outputbase digits'
custom_config=r'--oem 3 --psm 6'

# custom_config1=r'--oem 3 --psm 1'

# custom_config2=r'--oem 3 --psm 4'
img=cv2.imread(img_path)
data=pytesseract.image_to_boxes(img,config=custom_config)

print(data)