import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy.linalg import inv

class ColorFilter:
    def __init__(self):
        pass

    def invert(self, array):
        return [array]*150

    def to_blue(self, array):
        I_blue = array.copy()  # Duplicate image
        I_blue[:, :, 0] = 0    # Zero out contribution from green
        I_blue[:, :, 1] = 0
        return I_blue

    def to_green(self, array):
        I_green = array.copy()  # Duplicate image
        I_green[:, :, 0] = 0    # Zero out contribution from green
        I_green[:, :, 2] = 0
        return I_green

    def to_red(self, array):
        I_red = array.copy()  # Duplicate image
        I_red[:, :, 1] = 0    # Zero out contribution from green
        I_red[:, :, 2] = 0
        return I_red

    def to_grayscale(self,im, weights = np.c_[0.2989, 0.5870, 0.1140]):
        tile = np.tile(weights, reps=(im.shape[0],im.shape[1],1))
        return np.sum(tile * im, axis=2)


if __name__ == '__main__':
    img = mpimg.imread('../ex01/42AI.png')
    cf = ColorFilter()
    red = cf.to_red(img)
    blue = cf.to_blue(img)
    green = cf.to_green(img)
    grey = cf.to_grayscale(img)
    plt.imshow(grey)
    plt.show()