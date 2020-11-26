import cv2
import pytesseract
from pytesseract import Output
import matplotlib.pyplot as plt



def graphtextdetextor(image_path):
    """
    pass image path as an argument
    """
    img=cv2.imread(image_path)

    #img=image_filter.rotate_anticlockwise(img)

    custom_config_number=r'--oem 3 --psm 6 outputbase digits'
    custom_config=r'--oem 3 --psm 6'

    custom_config1=r'--oem 3 --psm 1'

    custom_config2=r'--oem 3 --psm 4'

    text2=pytesseract.image_to_string(img,config=custom_config1)
    
    # img=img[:,:max(100,img.shape[1]//2)]

    # plt.imshow(img)
    # plt.show()

    # print(img.shape[1]//5)
    text=pytesseract.image_to_string(img,config=custom_config)
    #text3=pytesseract.image_to_string(img,config=custom_config2)




    # print(text)



    d=pytesseract.image_to_data(img,config=custom_config,output_type=Output.DICT)

    n_boxes = len(d['text'])
    for i in range(n_boxes):
        if int(d['conf'][i]) > 60:
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)




    plt.imshow(img)
    plt.show()
    cv2.waitKey(0)

    return [text,text2]

if "__main__"== __name__:
    image_path='image1.png'
    d=graphtextdetextor(image_path)
    print(d)
    