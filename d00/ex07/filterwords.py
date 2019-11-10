import sys
import string

if __name__ == '__main__':
    try:
        s = str(sys.argv[1])
        n = int(sys.argv[2])
    except ValueError:
        print("InputError: arg1 is a string and arg2 is a number")
        exit()
    except BaseException:
        print("ERROR")
        exit()

    s = s.translate(str.maketrans('', '', string.punctuation))
    lst = []
    for word in s.split():
        if len(word) > n:
            lst.append(word)
    if not lst:
        print("ERROR")
    else:
        print(lst)