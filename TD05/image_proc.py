import matplotlib.pyplot as plt
import numpy as np
 
 
img = plt.imread("raccoon.png")
#Convert to int
img = img * 255
img = img.astype(int)
 
#Remove the transparency component
img = img[:,:,0:3]

def grayscale(img):
    return (img[:,:,0] * 0.3  + \
            img[:,:,1] * 0.59 + \
            img[:,:,2] * 0.11).astype(int)

gray_img = grayscale(img)

def histogram(gray_img):
    hist = np.zeros(256)
    np.add.at(hist, gray_img, 1)
    return hist / np.sum(hist)

def plot_intensity(gray_img):
    hist = histogram(gray_img)
    x = np.arange(len(hist))

    fig, (img_plt, hist_plt) = plt.subplots(1, 2, figsize=(15, 5))
    img_plt.set_title("Image")
    img_plt.imshow(gray_img, cmap="gray")

    hist_plt.plot(x, hist)
    hist_plt.fill_between(x, hist)
    hist_plt.set_xlabel("Intensity")
    hist_plt.set_ylabel("Percentage")
    hist_plt.set_title("Image Histogram")
    plt.show(block=True)

plot_intensity(gray_img)

def centile(gray_img):
    return np.percentile(gray_img, 2), np.percentile(gray_img, 98)

def find_corrections(gray_img):
    p2, p98 = centile(gray_img)

    contrast_vector = np.array([[0], [255]])
    centiles_vector = np.array([[p2, 1], [p98, 1]])
    corrections = np.linalg.solve(centiles_vector, contrast_vector)
    return corrections[0], corrections[1]

def auto_contrast(gray_img):
    img = np.zeros_like(gray_img)
    contrast_correction, intensity_contrast = find_corrections(gray_img)
    corrected_img = contrast_correction * gray_img[:, :] + np.full_like(gray_img, intensity_contrast)
    return np.clip(corrected_img[:,:], 0, 255)

plot_intensity(gray_img)
plot_intensity(auto_contrast(gray_img))