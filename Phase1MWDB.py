from pymongo import MongoClient
import cv2
import numpy as np
from PIL import Image
from scipy.stats import skew
import skimage.feature as ft
import glob
import features

try:
    client = MongoClient("mongodb://localhost:27017")
    print "success"
except:
    print "no success"

db = client.MWDB
# cm_feature_descriptors = db.cm_feature_descriptors
lbp = db.lbp_feature_descriptors

# extract all images
images = glob.glob('C:/Users/priya/Documents/SmallerDataset/*.jpg')

# loop through each image to calculate feature descriptor
for image in images:
    #print features.feature_descriptor(image, 'LBP')
    lbp.insert_one({"imageName": image, "LBP": features.feature_descriptor(image, 'LBP')})
    print "image"
