from threshold_fast import threshold_fast
import cv2
import matplotlib.pyplot as plt

i=cv2.imread('image2.png',0)
# image=threshold_fast(250,i)
plt.imshow(i,cmap="gray")
plt.show()
# k=cv2.imread('image2_filtered.png',0)
# plt.imshow(k,cmap="gray")
# plt.show()
print("done")