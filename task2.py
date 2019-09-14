from pymongo import MongoClient
import glob
import features

try:
    client = MongoClient("mongodb://localhost:27017")
    print "success"
except:
    print "no success"

db = client.MWDB

# extract all images
images = glob.glob('C:/Users/priya/Documents/SmallerDataset/*.jpg')

# Task 2
# loop through each image to calculate feature descriptor
for image in images:
    # Insert color moments' feature descriptors
    colorMoments, imageName = features.feature_descriptor(image, 'CM')
    db.cm.insert_one({"imageName": imageName, "CM": colorMoments})
    # Insert LBP feature descriptors
    lbpHist, imageName = features.feature_descriptor(image, 'LBP')
    db.lbp.insert_one({"imageName": imageName, "LBP": lbpHist})
