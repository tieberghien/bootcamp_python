class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        try:
            self.first_name = first_name
            assert isinstance(first_name, str)
        except:
            print("{} type provided for attribute 'first_name' instead of 'str'".format(type(first_name)))
            exit()
        self.is_alive = is_alive

class Stark(GotCharacter):
    """ A class representing the Stark family. Or when bad things happen to good people. """
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False