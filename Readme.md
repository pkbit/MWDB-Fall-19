# Feature Extraction of Hand Images
Features of Hand Images are extracted using Color Moments and LBP feature descriptors. Euclidean Distance measure is used to return 'k' most similar images for a given image.

# Image Dataset
https://sites.google.com/view/11khands

# Tools Used:
* Python 2.7.12
* NoSQL Database - MongoDB
* Pycharm community edition 2019.2.1
* Robo 3T 1.3

# Python libraries:
* cv2 - OpenCV library for image transformation
* numpy - Image and feature representation as an N-dimensional array
* PIL.image - Load image from files
* pymongo - MongoDB API for python
* skimage - Image transformation and LBP feature extraction of images
* os - extract file name from path
* glob - extract images with jpg extension from a given folder
* traceback - printup to limit stack trace entries

# Image feature extraction models - 
1.	Color Moments
2.	Local Binary Patterns

# Color Moments parameters:
* Window size: 100*100
* Color model - YUV
* feature vector - <mean(Y, U, V), variance(Y, U, V), skewness(Y, U, V)>
* Similarity function - Euclidean distance(L2 norm)
# LBP parameters:
* Window size: 100*100
* Color Model - Greyscale
* radius - 1
* histogram bins - 256
* Similarity function - Euclidean Distance(L2 norm)
