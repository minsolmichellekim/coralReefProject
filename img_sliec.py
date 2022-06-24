#import all necessary libraries
import image_slicer
from PIL import Image
from PIL import ImageStat
import math
from math import sqrt

#calculates ave brightness of pixels
def brightness(im_file):
   im = (im_file).convert('L') #removed "Image.open"
   stat = ImageStat.Stat(im)
   return stat.mean[0]

#slice the image and compute brightness for each slice
#make an array
#store all the brightness variables for each tile in said array
#
tiles = image_slicer.slice('IMG_3175.jpg', 50, save=False)
for tile in tiles:
    tile_br = brightness(tile.image)   
