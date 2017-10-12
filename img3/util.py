#!/anaconda/envs/mspenv/bin/python
import numpy as np
import cv2
import matplotlib.pyplot as plt


def sigma(f_c):
    s = 1 / (2 * np.pi * np.float32(f_c))
    return s

def gaussian_mask(sigma, shape):
    row, col = shape
    lpf = np.zeros(shape)
    for y in range(-row//2, row//2):
        for x in range(-col//2, col//2):
            lpf[y+row//2, x+col//2] = np.exp(-2*np.square(np.pi)*np.square(sigma)*(np.square(x)+np.square(y)))
    return lpf

def read_color_img(file_name):
    img = cv2.imread(filename=file_name, flags=cv2.IMREAD_COLOR)
    img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
    img = np.moveaxis(a=img, source=-1, destination=0)
    return img

def save_color_img(file_name, img):
    img = np.moveaxis(a=img, source=0, destination=-1)
    img = cv2.cvtColor(src=img, code=cv2.COLOR_RGB2BGR)
    cv2.imwrite(file_name, img)
    return

def save_grayscale_img(file_name, img):
    cv2.imwrite(file_name, img)
    return

def ft(img):
    img_ft = np.fft.fft2(a=img)
    img_ft_sft = np.fft.fftshift(x=img_ft)
    return img_ft_sft

def gaussian_filter(img_ft, mask):
    masked = np.multiply(img_ft, mask)
    return masked

def ift(img_ft_sft):
    img_ft = np.fft.ifftshift(x=img_ft_sft)
    img = np.fft.ifft2(a=img_ft)
    return np.abs(img).astype(np.uint8)

def hybrid(low, high, scale_low, scale_high):
    return np.add(np.multiply(scale_low, low), np.multiply(scale_high, high))

def show_color_img(img):
    img = np.moveaxis(a=img, source=0, destination=-1)
    plt.imshow(img)
    plt.show()
    return

def show_grayscale_img(img):
    plt.imshow(img, cmap='gray')
    plt.show()
    return

def read_grayscale_img(file_name):
    img = cv2.imread(filename=file_name, flags=cv2.IMREAD_GRAYSCALE)
    return img

def spectrum(img):
    return 20 * np.log(np.add(np.abs(img), 1))

def resize_color_img(img, dsize=None, fx=1, fy=1):
    img = np.moveaxis(a=img, source=0, destination=-1)
    img = cv2.resize(src=img, dsize=dsize, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    img = np.moveaxis(a=img, source=-1, destination=0)
    return img

def resize_grayscale_img(img, dsize=None, fx=1, fy=1):
    img = cv2.resize(src=img, dsize=dsize, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return img

def to_grayscale(img):
    img = np.moveaxis(a=img, source=0, destination=-1)
    img = cv2.cvtColor(src=img, code=cv2.COLOR_RGB2GRAY)
    return img

def gaussian_pyramid(img, depth):
    pyr = [img]
    for d in range(depth):
        img = cv2.pyrDown(src=pyr[-1])
        pyr.append(img)
    return pyr

def laplacian_pyramid(gaussian_pyr):
    lpyr = []
    for low, high in zip(gaussian_pyr[:-1], gaussian_pyr[1:]):
        expanded = cv2.pyrUp(src=high, dstsize=low.shape[::-1])
        img = cv2.subtract(low, expanded)
        img = cv2.resize(src=img, dsize=gaussian_pyr[0].shape[::-1], interpolation=cv2.INTER_LINEAR)
        lpyr.append(img)
    return lpyr[::-1]

def enhance(img, clipLimit=40, tileGridSize=(8, 8)):
    clahe = cv2.createCLAHE(clipLimit=clipLimit, tileGridSize=tileGridSize)
    img = clahe.apply(img)
    return img

# def save_color_img(file_name, img):
#     img = np.moveaxis(a=img, source=0, destination=-1)
#     cv2.imwrite(file_name, img)
#     return
# def show_color_img(img):
#     img = 
#     rgb_img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2RGB)
#     plt.imshow(rgb_img)
#     plt.show()
#     return


# def read_color_img(file_name):
#     img = cv2.imread(filename=file_name, flags=cv2.IMREAD_COLOR)
#     return np.moveaxis(a=img, source=-1, destination=0)

# def read_grayscale_img(file_name):
#     img = cv2.imread(filename=file_name, flags=cv2.IMREAD_GRAYSCALE)
#     return img


#     # img = cv2.idft(src=img_ft, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)