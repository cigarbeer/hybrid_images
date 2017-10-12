import util as ut
import setting as st


if __name__ == '__main__':
    lsrc_name = './src/low.jpg'
    hsrc_name = './src/high.jpg'
    hybrid_path = './result/'

    print('read imgs...')
    lsrc = ut.read_color_img(lsrc_name)
    hsrc = ut.read_grayscale_img(hsrc_name)

    print('fourier transform imgs...')
    lsrc_ft = ut.ft(lsrc)
    hsrc_ft = ut.ft(hsrc)

    print('creating hybrid imgs...')
    shape = hsrc.shape
    fc = st.fc
    fgap = st.fgap
    lpf = []
    hpf = []
    for i in range(len(fc)):
        sigma = ut.sigma(fc[i])
        lpf.append(ut.gaussian_mask(sigma, shape))
        for j in range(len(fgap)):
            sigma = ut.sigma(fc[i]+fgap[j])
            hpf.append(1-ut.gaussian_mask(sigma, shape))

            lres_ft = ut.gaussian_filter(lsrc_ft, lpf[i])
            hres_ft = ut.gaussian_filter(hsrc_ft, hpf[j])

            hybridimg_ft = ut.hybrid(lres_ft, hres_ft, st.scale_low, st.scale_high)

            hybridimg = ut.ift(hybridimg_ft)

            hybrid_name = hybrid_path+'l'+str(fc[i])+'h'+str(fc[i]+fgap[j])+'.jpg'
            ut.save_color_img(hybrid_name, hybridimg)

            print(hybrid_name)