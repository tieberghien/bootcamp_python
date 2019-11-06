from datetime import timedelta

def generator(text, sep=" ", option=None):
    '''Option is an optional arg, sep is mandatory'''
    for w in text.split(sep):
        yield w

if __name__ == '__main__':
    text = "Le Lorem Ipsum est simplement du faux texte."
    for word in generator(text, sep=" "):
        print(word)