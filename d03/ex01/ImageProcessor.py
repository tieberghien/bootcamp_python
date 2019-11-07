import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        img = mpimg.imread('42AI.png')
        print("Loading image of dimensions {} x {}".format(img.shape[0], img.shape[1]))
        return img

    def display(self, array):
        plt.imshow(array)
        plt.show()

if __name__ == '__main__':
    imp = ImageProcessor()
    img = imp.load('42AI.png')
    imp.display(img)