import traceback
from pymongo import MongoClient
import constants


def euclidean_dist(vectorA, vectorB):
    squares = 0
    for i in range(len(vectorA)):
        squares = squares + (vectorA[i] - vectorB[i]) ** 2
    return squares ** 0.5


def kSimilarFeatures(imgFeature, featureDescriptors, model, k):
    distance = []
    if model == "CM":
        for feature in featureDescriptors:
            dist = euclidean_dist(feature['CM'], imgFeature['CM'])
            distance.append([feature['imageName'], dist])
    else:
        for feature in featureDescriptors:
            dist = euclidean_dist(feature['LBP'], imgFeature['LBP'])
            distance.append([feature['imageName'], dist])

    return sorted(distance, key=lambda x: x[1])[:k]


def main():
    imageId, model, k = raw_input("Enter imageID, model(ColorMoments/LBP) and k: ").split()
    imageId = imageId + ".jpg"
    try:
        client = MongoClient("mongodb://localhost:27017")
        db = client.MWDB

        if model == 'CM':
            imageFeature = db.cm.find_one({'imageName': imageId})
            if imageFeature is not None:
                featureDescriptors = db.cm.find({'imageName': {"$ne": imageId}})
                print kSimilarFeatures(imageFeature, featureDescriptors, model, int(k))
        elif model == 'LBP':
            imageFeature = db.lbp.find_one({'imageName': imageId})
            if imageFeature is not None:
                featureDescriptors = db.lbp.find({'imageName': {"$ne": imageId}})
                print kSimilarFeatures(imageFeature, featureDescriptors, model, int(k))
        else:
            print "Input model entered is incorrect."

    except Exception as detail:
        traceback.print_exc()
        print "no success"


if __name__ == '__main__':
    main()
