class Vector:
    def __init__(self, values, length):
        try:
            self.values = values
            assert isinstance(values, list)
        except:
            print("{} type provided for attribute 'values' instead of 'list'".format(type(values)))
            exit()
        try:
            self.length = length
            assert isinstance(length, int)
        except:
            print("{} type provided for attribute 'length' instead of 'int'".format(type(length)))
            exit()

    def __add__()