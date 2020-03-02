from threshold_fast import threshold_fast
import cv2
import matplotlib.pyplot as plt

i=cv2.imread('test.png',2)
image=threshold_fast(250,i)
plt.imshow(image,cmap="gray")
plt.show()
print("done")