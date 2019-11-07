import numpy as np

class NumPyCreator:
    def __init__(self):
        pass
    
    def from_list(self, lst):
        return np.asarray(lst)

    def from_tuple(self, tpl):
        return np.asarray(tpl)

    def from_iterable(self, itr):
        return np.fromiter(itr, int)
    
    def from_shape(self, shape, value):
        pass
    
    def random(self, shape):
        pass

    def identity(self, n):
        pass

if __name__ == '__main__':
    npc = NumPyCreator()
    print(npc.from_list([[1,2,3],[6,3,4]]))
    print(npc.from_tuple(("a", "b", "c")))
    print(npc.from_iterable(range(5)))