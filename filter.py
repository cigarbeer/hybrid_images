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



if __name__ == '__main__':
    fc = [3, 6, 9, 12, 15, 18, 21]
    fgap = [0, 5, 10, 15, 20, 25]

    f_low = fc
    f_high = []

    for f in fc:
        for g in fgap:
            f_high.append(f+g)

    for f in f_low:
        plt.imshow(gaussian_mask(sigma(f), (f*5, f*5)), cmap='gray')
        plt.savefig('./filter/lpf'+str(f)+'.jpg')

    for f in f_high:
        plt.imshow(1-gaussian_mask(sigma(f), (f*5, f*5)), cmap='gray')
        plt.savefig('./filter/hpf'+str(f)+'.jpg')
