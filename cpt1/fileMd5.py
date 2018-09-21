import hashlib
import sys


def getMd5(file):
    fd=open(file,'rb')
    fcont = fd.read()
    print(hashlib.md5(fcont).hexdigest(),file)


if __name__ == "__main__":
    # print(sys.argv)
    if len(sys.argv) > 2:
        for st in sys.argv[1:]:
            getMd5(st)
    elif len(sys.argv) == 2:
        getMd5(sys.argv[1])
    else:
        print("input file name.")
        print("output like this: ")
        getMd5('49467_628649_new132.png')

