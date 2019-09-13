import cv2
import numpy as np
from PIL import Image
from bson import decimal128
from scipy.stats import skew
import skimage.feature as ft
from bson.decimal128 import Decimal128


def feature_descriptor(imageName, colorModel):
    image = cv2.imread(imageName)
    imago = Image.open(imageName)

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
        mean_arr_y = []
        mean_arr_u = []
        mean_arr_v = []
        mean = []
        # standard deviation
        dev_arr_y = []
        dev_arr_u = []
        dev_arr_v = []
        dev = []
        # skewness
        skew_arr_y = []
        skew_arr_u = []
        skew_arr_v = []
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
                mean_arr_y.append(np.mean(arr_y))
                mean_arr_u.append(np.mean(arr_u))
                mean_arr_v.append(np.mean(arr_v))
                # standard deviation
                dev_arr_y.append(np.std(arr_y))
                dev_arr_u.append(np.std(arr_u))
                dev_arr_v.append(np.std(arr_v))
                # skewness
                skew_arr_y.append(skew(arr_y.flatten()))
                skew_arr_u.append(skew(arr_u.flatten()))
                skew_arr_v.append(skew(arr_v.flatten()))
        mean = np.concatenate((mean_arr_y, mean_arr_u, mean_arr_v))
        dev = np.concatenate((dev_arr_y, dev_arr_u, dev_arr_v))
        skew1 = np.concatenate((skew_arr_y, skew_arr_u, skew_arr_v))
        return mean, dev, skew
    elif colorModel == 'LBP':
        #########################
        # LBP
        #########################
        img_lbp = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        temp = []
        arr_lbp = []
        radius = 50
        length = 8 * radius
        for i in range(red_height):
            for j in range(red_width):
                temp_arr = img_lbp[i * 100:(i * 100) + 100, j * 100:(j * 100) + 100]
                temp, bin_ed = np.histogram(ft.local_binary_pattern(temp_arr, length, 50), bins=256, density=True)
                arr_lbp.append(temp)
        return arr_lbp
