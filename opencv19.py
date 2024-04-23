import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('jjang.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, cheak with os.path.exists()"