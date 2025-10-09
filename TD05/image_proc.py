import matplotlib.pyplot as plt
import numpy as np

 
img = plt.imread("./TD05/raccoon.png")
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

def centile(gray_img):
    return np.percentile(gray_img, 2), np.percentile(gray_img, 98)

def find_corrections(gray_img):
    p2, p98 = centile(gray_img)

    contrast_vector = np.array([[0], [255]])
    centiles_vector = np.array([[p2, 1], [p98, 1]])
    corrections = np.linalg.solve(centiles_vector, contrast_vector)
    return corrections[0], corrections[1]

def auto_contrast(gray_img):
    contrast_correction, intensity_contrast = find_corrections(gray_img)
    corrected_img = (contrast_correction * gray_img[:, :] + np.full_like(gray_img, intensity_contrast))
    return np.clip(corrected_img[:, :], 0, 255).astype(int)

corrected_gray_img = auto_contrast(gray_img)
plot_intensity(gray_img)
plot_intensity(corrected_gray_img)

def plot_color_intensities(img):
    bins_r = histogram(img[:,:,0])
    bins_g = histogram(img[:,:,1])
    bins_b = histogram(img[:,:,2])
    x = np.linspace(0, 255, 256)
 
    fig, (img_plt, hist_plt) = plt.subplots(1, 2, figsize=(15, 5))
    img_plt.set_title("Image")
    img_plt.imshow(img, norm=None)

    hist_plt.plot(x, bins_r)
    hist_plt.plot(x, bins_g)
    hist_plt.plot(x, bins_b)
    hist_plt.fill_between(x, bins_r, color="#FF000055")
    hist_plt.fill_between(x, bins_g, color="#00FF0055")
    hist_plt.fill_between(x, bins_b, color="#0000FF55")
    hist_plt.set_xlabel("Intensity")
    hist_plt.set_ylabel("Percentage")
    hist_plt.set_title("Image Histogram")
    plt.show(block=True)

def to_YCbCr(img):
    v = np.array([0, 128, 128])
    rgb2ycbcr = np.array([[0.299, 0.587, 0.114], [-0.168736, -0.331264, 0.5], [0.5, -0.418688, -0.081312]])
    tmp = np.dot(img, rgb2ycbcr.T)+v
    tmp = tmp.astype(int)
    return np.clip(tmp, 0, 255)
 
def to_RGB(img):
    v = np.array([0, 128, 128])
    ycbcr2rgb = np.array([[1, 0, 1.402], [1, -0.344136, -0.714136], [1, 1.772, 0]])
    tmp = img-v
    tmp = np.dot(tmp, ycbcr2rgb.T)
    tmp = tmp.astype(int)
    return np.clip(tmp, 0, 255)
 
 
def test_convertion(img):
    ycc = to_YCbCr(img)
    rgb = to_RGB(ycc)
    diff = np.absolute(img - rgb)
    print("Min, Max and Mean, of differences between original image and convert-reconvert image : {}, {}, {}".format(
                np.min(diff), np.max(diff), np.mean(diff)))  

def auto_contrast_YCbCr(img):
    ycbcr = to_YCbCr(img)
    ycbcr[:,:,0] = auto_contrast(ycbcr[:,:,0])
    return to_RGB(ycbcr)
 
corrected_img = auto_contrast_YCbCr(img)
plot_color_intensities(img)
plot_color_intensities(corrected_img)