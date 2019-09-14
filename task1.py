import traceback

from pymongo import MongoClient
import features


def main():
    try:
        client = MongoClient("mongodb://localhost:27017")
        print "success"

        db = client.MWDB

        # extract all images
        imageID, model = raw_input("Enter ImageID and the model(ColorMoments/LBP): ").split()
        image = 'C:/Users/priya/Documents/SmallerDataset/' + imageID + '.jpg'
        if model == 'ColorMoments':
            feature_descriptor, img = features.feature_descriptor(image, 'CM')
        else:
            feature_descriptor, img = features.feature_descriptor(image, 'LBP')
        print feature_descriptor

    except Exception as detail:
        traceback.print_exc()
        print "no success"


if __name__ == '__main__':
    main()
