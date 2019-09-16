from pymongo import MongoClient
import glob
import features
import constants
import traceback

try:
    client = MongoClient("mongodb://localhost:27017")

    db = client.MWDB

    # extract all images
    images = glob.glob(constants.read_path+'*.jpg')

    # Task 2
    # loop through each image to calculate feature descriptor
    for image in images:
        # Insert color moments' feature descriptors
        colorMoments, imageName = features.feature_descriptor(image, 'CM')
        db.cm.insert_one({"imageName": imageName, "CM": colorMoments})
        # Insert LBP feature descriptors
        lbpHist, imageName = features.feature_descriptor(image, 'LBP')
        db.lbp.insert_one({"imageName": imageName, "LBP": lbpHist})

except Exception as detail:
    traceback.print_exc()
    print "no success"
