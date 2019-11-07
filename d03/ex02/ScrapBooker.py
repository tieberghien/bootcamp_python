import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ScraperBooker:
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0,0)):
        return array[position[0]:dimensions, position[1]:dimensions]

    def thin(self, array, n, axis):
        pass

    def juxtapose(self, array, n, axis):
        pass

    def mosaic(self, array, dimensions):
        pass

if __name__ == '__main__':
    img = mpimg.imread('../ex01/42AI.png')
    print(img.shape[0], img.shape[1])
    sb = ScraperBooker()
    cropped = sb.crop(img, 100, (50,50))
    plt.imshow(cropped)
    plt.show()