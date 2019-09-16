import constants
import features


def main():

    # extract all images
    imageID, model = raw_input("Enter ImageID and the model(CM/LBP): ").split()
    image = constants.read_path + imageID + '.jpg'
    if model == 'CM':
        feature_descriptor, img = features.feature_descriptor(image, 'CM')
        print feature_descriptor
    elif model == 'LBP':
        feature_descriptor, img = features.feature_descriptor(image, 'LBP')
        print feature_descriptor
    else:
        print "Input model entered is incorrect."


if __name__ == '__main__':
    main()
