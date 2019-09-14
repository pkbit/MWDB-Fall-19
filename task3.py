import traceback
from pymongo import MongoClient


def euclidean_dist(vectorA, vectorB):
    squares = 0
    for i in range(len(vectorA)):
        squares = squares + (vectorA[i] - vectorB[i]) ** 2
    return squares ** 0.5


def kSimilarFeatures(imgFeature, featureDescriptors, model, k):
    distance = []
    if model == "ColorMoments":
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
        print "success"
        db = client.MWDB

        if model == "ColorMoments":
            imageFeature = db.cm.find_one({'imageName': imageId})
            if imageFeature is not None:
                featureDescriptors = db.cm.find({'imageName': {"$ne": imageId}})
                print kSimilarFeatures(imageFeature, featureDescriptors, model, int(k))
        else:
            imageFeature = db.lbp.find_one({'imageName': imageId})
            if imageFeature is not None:
                featureDescriptors = db.lbp.find({'imageName': {"$ne": imageId}})
                print kSimilarFeatures(imageFeature, featureDescriptors, model, int(k))

    except Exception as detail:
        traceback.print_exc()
        print "no success"


if __name__ == '__main__':
    main()
