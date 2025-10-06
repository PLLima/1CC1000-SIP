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