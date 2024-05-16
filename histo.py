import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--image', help='enter the image path')
parser.add_argument('--output', help='enter the output path')


args = vars(parser.parse_args())
image = cv2.imread(args['image'])
cv2.imwrite(args["output"], image)

 
assert image is not None, "file could not be read, check with os.path.exists()"
color = ('b','g','r')
for i,col in enumerate(color):
 histr = cv2.calcHist([image],[i],None,[256],[0,256])
 plt.plot(histr,color = col)
 plt.xlim([0,256])
plt.show()