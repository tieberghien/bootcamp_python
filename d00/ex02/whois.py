import sys

if __name__ == '__main__':
    try:
        n = sys.argv[1]
    except:
        exit()
    if len(sys.argv) > 2:
        print("ERROR")
        exit()
    if n.isdigit():
        if (int(n) % 2) == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    else:
        print("ERROR")