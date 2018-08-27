import sys
import os

def main():
    argv = sys.argv
    argl = len(argv)
    if (argl != 2):
        print 'Usage: python %s arg1 arg2' %argv[0]
        quit()
    else:
        root = argv[1]
        new = argv[2]
    



if __name__ = '__main__':
    main()