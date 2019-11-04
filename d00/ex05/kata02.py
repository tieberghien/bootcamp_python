def rev_tuples(tuples): 
    new_tup = tuples[::-1] 
    return new_tup

if __name__ == '__main__':
    tuples = (3,30,2019,9,25)
    reverse = rev_tuples(tuples)
    print('{}/{}/{} {}:{}'.format(str(reverse[0]), str(reverse[1]), str(reverse[2]), str(reverse[3]), str(reverse[4])))