import sys

# WARNING STRING FORMAT '%' OBSOLETE

if __name__ == '__main__':
    try:
        n1 = float(sys.argv[1])
        n2 = float(sys.argv[2])
    except ValueError:
        print("InputError: only number")
        print("Usage: python operations.py\nExample:\n  python operations.py 10 3")
        exit()
    except BaseException:
        print("Usage: python operations.py\nExample:\n  python operations.py 10 3")
        exit()
    print("Sum: %d" % int(n1+n2))
    print("Difference: %d" % int(n1-n2))
    print("Product: %d" % int(n1*n2))
    try:
        print("Quotient: %f" % (n1/n2))
    except ZeroDivisionError as e:
        print("Quotient: ERROR (div by zero)")
    try:
        print("Remainder: %d" % int(n1%n2))
    except ZeroDivisionError as e:
        print("Remainder: ERROR (modulo by zero)")