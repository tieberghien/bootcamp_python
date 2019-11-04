import sys

if __name__ == '__main__':
    str = []
    try:
        for i in range(1, len(sys.argv)):
            str.append(sys.argv[i])
            reversed=" ".join(str)[::-1]
    except:
        exit()
    print(reversed)