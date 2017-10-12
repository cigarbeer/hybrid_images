import cv2
import util as ut
import numpy as np
import sys
import setting as st

if __name__ == '__main__':
    hybridimg_name = './result/' + st.lpyr_img_name
    depth = st.lpyr_depth
    laplacian_pyr_path = st.lpyr_path

    hybridimg = ut.read_grayscale_img(hybridimg_name)

    gpyr = ut.gaussian_pyramid(hybridimg, int(depth))

    lpyr = ut.laplacian_pyramid(gpyr)

    for i in range(len(lpyr)):
        name = laplacian_pyr_path+hybridimg_name.split('/')[-1].split('.')[0]+'_lpyr'+str(i)+'.jpg'
        print(name)
        img = lpyr[i]
        ut.save_grayscale_img(name, ut.enhance(img=img, clipLimit=st.clipLimit, tileGridSize=st.tileGridSize))

