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


def boundingbox(image_path):

    custom_config=r'--oem 3 --psm 6'

    image = cv2.imread(image_path)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_data(rgb, config=custom_config,output_type=Output.DICT)

    for i in range(0, len(results["text"])):

        x=results["left"][i]
        y=results["top"][i]
        w=results["width"][i]
        h=results["height"][i]

        text=results["text"][i]
        conf=int(results["conf"][i])

        #filter out weak confidence text localizations

        if conf>0:
            text="".join([c if ord(c)<128 else "" for c in text]).strip()
            cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(image, text, (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    print("here")

    plt.imshow(image)
    plt.show()
    cv2.waitKey(0)



if "__main__"== __name__:
    image_path='please3.png'
    boundingbox(image_path)
    # d=graphtextdetextor(image_path)
    # print(d)
    