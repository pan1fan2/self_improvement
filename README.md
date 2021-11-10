# Teach myself on deep learning

The repo contains codes for self imporvement. 

##### [Project 1: Image classification using Pytorch via NN](https://github.com/pan1fan2/self_improvement/tree/main/project1)

Builid a image classifier using Pytroch and to distiguish cat image from fishes but the model only applies simple neuro network

##### Project 2: Image classification using Pytorch via CNN

CNN model vision of project 1

##### [Project 3: Image classification using Tensorflow vis CNN+Transfer learning](https://github.com/pan1fan2/self_improvement/tree/main/project3)

Build a effective CNN model for image classification. 

##### [Project 4 : Generative Adversarial Network (GAN) using Pytorch] (https://github.com/pan1fan2/self_improvement/tree/main/project4)

Learn and test a simple GAN model on 

![](https://github.com/pan1fan2/self_improvement/blob/main/image/gan.png)

##### Project 5: Steel defect detection

The kaggle competition page can be found [here](https://www.kaggle.com/c/severstal-steel-defect-detection/overview)

Each image may have no defects, a defect of a single class, or defects of multiple classes. For each image you must segment defects of each class (ClassId = [1, 2, 3, 4]).

The segment for each defect class will be encoded into a single row, even if there are several non-contiguous defect locations on an image.

Files

- train_images/ - folder of training images
- test_images/ - folder of test images (you are segmenting and classifying these images)
- train.csv - training annotations which provide segments for defects (ClassId = [1, 2, 3, 4])
- sample_submission.csv - a sample submission file in the correct format; note, each ImageId 4 rows, one for each of the 4 defect classes



