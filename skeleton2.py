from skimage import img_as_bool, io, color, morphology
import matplotlib.pyplot as plt

image = img_as_bool(color.rgb2gray(io.imread('test.png')))
out = morphology.medial_axis(image)

f, (ax0, ax1) = plt.subplots(1, 2)
ax0.imshow(image, cmap='gray', interpolation='nearest')
ax1.imshow(out, cmap='gray', interpolation='nearest')
plt.show()