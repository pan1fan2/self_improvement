##### Project 5: Steel defect detection

The kaggle competition page can be found [here](https://www.kaggle.com/c/severstal-steel-defect-detection/overview)

Each image may have no defects, a defect of a single class, or defects of multiple classes. For each image you must segment defects of each class (ClassId = [1, 2, 3, 4]).

The segment for each defect class will be encoded into a single row, even if there are several non-contiguous defect locations on an image.

Files

- train_images/ - folder of training images
- test_images/ - folder of test images (you are segmenting and classifying these images)
- train.csv - training annotations which provide segments for defects (ClassId = [1, 2, 3, 4])
- sample_submission.csv - a sample submission file in the correct format; note, each ImageId 4 rows, one for each of the 4 defect classes

Neu data: Trained with [YOLO](https://github.com/ultralytics/yolov5) 

Files

The dataset contains defects of 6 classes. (crazing','inclusion','patches','pitted_surface','rolled-in_scale','scratches')

- train/ - folder contains training images and corresponding labels (~1700)
- Valid/ - folder contains validation images and corresponding labels (~50)

Results:

![train_batch1](https://github.com/pan1fan2/self_improvement/blob/main/project5/train_batch0.jpg)
