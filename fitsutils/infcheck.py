#! /usr/bin/env python3
from ast import arg
from astropy.io import fits
import argparse
import numpy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="+")
    args = parser.parse_args()

    for filename in args.filenames:
        hdus = fits.open(filename)
        data = hdus[0].data

        if data is None:
            print (f"{filename}: not an image")
        else:
            posinfs = numpy.argwhere(numpy.isposinf(data))
            neginfs = numpy.argwhere(numpy.isneginf(data))
            nans = numpy.argwhere(numpy.isnan(data))

            if len(posinfs) == 0 and len(neginfs) == 0 and len(nans) == 0:
                print (f"{filename}: OK")
            else:
                if len(posinfs) > 0:
                    print (f"{filename}: {len(posinfs)} positive infinities detected: {posinfs}")
                if len(neginfs) > 0:
                    print (f"{filename}: {len(neginfs)} negative infinities detected: {neginfs}")
                if len(nans) > 0:
                    print (f"{filename}: {len(nans)} not-a-numbers detected: {nans}")
if __name__ == '__main__':
    main()