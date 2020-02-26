import cv2

im = cv2.imread('image2.png')

print(type(im))
# <class 'numpy.ndarray'>

print(im.shape)
print(type(im.shape))
# (225, 400, 3)
# <class 'tuple'>
h, w, c = im.shape
print('width:  ', w)
print('height: ', h)
print('channel:', c)
# width:   400
# height:  225
# channel: 3