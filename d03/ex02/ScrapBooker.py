import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ScraperBooker:
    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0,0)):
        try:
            assert dimensions[0] < array.shape[0] and dimensions[1] < array.shape[1]
        except:
            print("'dimensions' can't be larger than size of image")
            exit()
        return array[position[0]:dimensions[0], position[1]:dimensions[1]]

    def thin(self, array, n, axis):
        return np.delete(array, np.s_[::n], axis)

    def juxtapose(self, array, n, axis):
        if axis == 0:
            return np.vstack([array]*n)
        elif axis == 1:
            return np.hstack([array]*n)
        else
            print("Only accepts 2d images")
            exit()

    def mosaic(self, array, dimensions):
        array = np.concatenate([array]*dimensions[0], axis=0)
        array = np.concatenate([array]*dimensions[1], axis=1)
        return array

if __name__ == '__main__':
    img = mpimg.imread('../ex01/42AI.png')
    sb = ScraperBooker()
    cropped = sb.crop(img, (100, 150), (50,50))
    thinned = sb.thin(img, 2, 0)
    juxt = sb.juxtapose(img, 3, 0)
    mosaic = sb.mosaic(img, (2,3))
    plt.imshow(mosaic)
    plt.show()