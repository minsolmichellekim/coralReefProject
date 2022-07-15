#preprocessing for UNET
from PIL import Image
import cv2, os
import numpy as np
from pathlib import Path

image_list = []

directory = 'masks'
directory2 = 'images'

#Convert masks to binary
for filename in os.listdir(directory):
     im = cv2.imread(os.path.join(directory,filename))

     # converting to its binary form
     bw, ret = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)

     # store binary version in folder
     if ret is not None: 
          path = '/Users/janyagambhir/cats/TrainYourOwnYOLO/masks'
          new_filename = filename + "_mask"
          cv2.imwrite(os.path.join(path, new_filename), ret)

#Rotate all images and convert to TIF
for filename in os.listdir(directory2):
       im = cv2.imread(os.path.join(directory2,filename))

       if im is not None: 
          width, height, c = im.shape 

          #standardize all images to landscape 
          if height > width: 
               im = cv2.rotate(im, cv2.ROTATE_90_COUNTERCLOCKWISE)

          #Convert to TIF
          path = '/Users/janyagambhir/cats/TrainYourOwnYOLO/images'
          new_filename = Path(filename).stem + ".tif"

          cv2.imwrite(os.path.join(path, new_filename), im)
     