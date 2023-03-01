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
            flat = data.flatten()
            print ("-" * 10, filename, "-" * 10)
            print("    min/max", flat.min(), flat.max())
            print("    min/max without nans", flat[numpy.nanargmin(flat)], flat[numpy.nanargmax(flat)])
            
            posinfs = numpy.argwhere(numpy.isposinf(data))
            print("    +infs", len(posinfs), posinfs)
            
            neginfs = numpy.argwhere(numpy.isneginf(data))
            print("    -infs", len(neginfs), neginfs)

            nans = numpy.argwhere(numpy.isnan(data))
            print("    nans", len(nans), nans)

if __name__ == '__main__':
    main()