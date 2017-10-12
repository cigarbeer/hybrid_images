#   IMPORTANT: SINCE CEIBA HAS UPLOAD LIMIT 15MB, I CANNOT UPLOAD THE COMPLETE VERSION. TO GET ALL RESULTS PLEASE FOLLOW THE 'How to reproduce the results' part below. OR CHECK MY GITHUB 

#   Files
*   There are 4 Experiments:
    1.  img1/
    2.  img2/
    3.  img3/
    4.  img4/ 
*   img*/ contains:
    +   src/ contains 2 preprocessed source images
        -   high.jpg
        -   low.jpg
    +   result/ contains hybrid images with different cutoff frequency combinations
        -   l*h*.jpg (e.g. l9h29 means LPF cutoff=9 and HPF cutoff=29)
    +   laplacianpyramid/ contains laplacian pyramid of a chosen cutoff frequency combination
        -   l*h*_lpyr*.jpg
    +   hybridimg.py: the scirpt that generates hybrid images from src and saves them to img*/result/
    +   laplacianpyramid.py: the script that generate laplacian pyramid from a chosen hybrid image and saves them to img*/laplacianpyramid/
    +   util.py: define some functions used by hybridimg.py and laplacianpyramid.py
    +   setting.py: define some values used by hybridimg.py and laplacianpyramid.py such as cutoff frequencies, frequency gaps, scaling weights...
*   filter/ contains visualized filter images:
    +   hpf*.jpg (e.g. hpf20 means HPF with cutoff=20)
    +   lpf*.jpg (e.g. lpf12 means LPF with cutoff=12)
*   filter.py: the script that visulize the fliters and save them in ./filter/
*   report.pdf

#   How to reproduce the results
*   Note: You have to use python3.5 and install opencv3, numpy, matplotlib first
*   Note: It may take about 15 minutes to generate all hybrid images since the computation of gaussian filter is time-consuming
+   hybrid images
    -   $ cd img*
    -   $ python hybridimg.py
+   laplacian pyramids
    -   $ cd img*
    -   $ python laplacianpyramid.py
+   filter images
    -   $ python filter.py