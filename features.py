import cv2
import numpy as np
from PIL import Image
from scipy.stats import skew
import skimage.feature as ft
import os


def feature_descriptor(imageName, colorModel):
    image = cv2.imread(imageName)
    imago = Image.open(imageName)
    head, tail = os.path.split(imago.filename)
    # matrix dimensions before slicing
    width, height = imago.size

    # matrix dimensions after slicing
    red_width = width / 100
    red_height = height / 100


    #########################
    # color moments
    #########################
    if colorModel == 'CM':
        # mean
        mean_y = []
        mean_u = []
        mean_v = []
        mean = []
        # standard deviation
        dev_y = []
        dev_u = []
        dev_v = []
        dev = []
        # skewness
        skew_y = []
        skew_u = []
        skew_v = []
        skew1 = []
        # convert from RGB to YUV
        img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        y, u, v = cv2.split(img_yuv)

        for i in range(red_height):
            for j in range(red_width):
                # slicing matrix
                arr_y = y[i * 100:(i * 100) + 99, j * 100:(j * 100) + 99]
                arr_u = u[i * 100:(i * 100) + 99, j * 100:(j * 100) + 99]
                arr_v = v[i * 100:(i * 100) + 99, j * 100:(j * 100) + 99]
                # mean
                mean_y.append(np.mean(arr_y))
                mean_u.append(np.mean(arr_u))
                mean_v.append(np.mean(arr_v))
                # standard deviation
                dev_y.append(np.std(arr_y))
                dev_u.append(np.std(arr_u))
                dev_v.append(np.std(arr_v))
                # skewness
                skew_y.append(skew(arr_y.flatten()))
                skew_u.append(skew(arr_u.flatten()))
                skew_v.append(skew(arr_v.flatten()))
        concatCM = np.concatenate((mean_y, mean_u, mean_v, dev_y, dev_u, dev_v, skew_y, skew_u, skew_v)).tolist()
        return concatCM, tail
    #########################
    # LBP
    #########################
    elif colorModel == 'LBP':
        img_lbp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        radius = 50
        length = 8 * radius
        for i in range(red_height):
            for j in range(red_width):
                block = img_lbp[i * 100:(i * 100) + 100, j * 100:(j * 100) + 100]
                lbp = ft.local_binary_pattern(block, length, radius, 'default').reshape(10000, )
                temp, bin_ed = np.histogram(lbp, bins=np.arange(257), density=True)
                if i == 0 and j == 0:
                    arr_lbp = np.array(temp)
                else:
                    arr_lbp = np.concatenate([arr_lbp, temp])
        return arr_lbp.tolist(), tail
