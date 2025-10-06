import matplotlib.pyplot as plt
import numpy as np
 
 
img = plt.imread("raccoon.png")
#Convert to int
img = img * 255
img = img.astype(int)
 
#Remove the transparency component
img = img[:,:,0:3]
plt.imshow(img, norm=None)
plt.show()

def grayscale(img):
    return (img[:,:,0] * 0.3  + \
            img[:,:,1] * 0.59 + \
            img[:,:,2] * 0.11).astype(int)

gray_img = grayscale(img)
plt.imshow(gray_img, cmap="gray")
plt.show()

def histogram(gray_img):
    hist = np.zeros(256)
    np.add.at(hist, gray_img, 1)
    return hist / np.sum(hist)

print(histogram(gray_img))