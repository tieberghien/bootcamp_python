import string

def text_analyzer(text={}):
    """ This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
    if text is text_analyzer.__defaults__[0]:
        try:
            str = input("What is the text to analyse?\n>> ")
        except:
            exit()
    else:
        str = text
    count = 0
    upper = 0
    lower = 0
    punc = 0
    space = 0
    for i in range(len(str)):
        if str[i].isupper():clea
            upper += 1
        elif str[i].islower():
            lower += 1
        elif str[i] in string.punctuation:
            punc += 1
        elif str[i].isspace():
            space += 1
        count += 1
    print("The text contains %d characters" % count)
    print("- %d upper letters" % upper)
    print("- %d lower letters" % lower)
    print("- %d punctuation marks" % punc)
    print("- %d spaces" % space)