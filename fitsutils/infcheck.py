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

        for i in range(len(hdus)):
            hdu = hdus[i]
            process_hdu(hdu, filename, i)

def process_hdu(hdu, filename, index):
    if isinstance(hdu, fits.PrimaryHDU):
        process_image(hdu, filename, index)
    elif isinstance(hdu, fits.BinTableHDU):
        pass
        process_table(hdu, filename, index)
    else:
        print(f"{filename}.{index}: skipping")


def process_image(hdu, filename, index):
    data = hdu.data
    if data is None:
        print (f"{filename}.{index}: Not an image")
    else:
        posinfs = numpy.argwhere(numpy.isposinf(data))
        neginfs = numpy.argwhere(numpy.isneginf(data))
        nans = numpy.argwhere(numpy.isnan(data))

        if len(posinfs) == 0 and len(neginfs) == 0 and len(nans) == 0:
            print (f"{filename}.{index}: OK")
        else:
            if len(posinfs) > 0:
                print (f"{filename}.{index}: {len(posinfs)} positive infinities detected: {posinfs}")
            if len(neginfs) > 0:
                print (f"{filename}.{index}: {len(neginfs)} negative infinities detected: {neginfs}")
            if len(nans) > 0:
                print (f"{filename}.{index}: {len(nans)} not-a-numbers detected: {nans}")

def process_table(hdu, filename, index):
    data = hdu.data
    if data is None:
        print (f"{filename}.{index}: Not a table")
    else:
        posinfs, neginfs, nans = handle_data(data)
        if posinfs == 0 and neginfs == 0 and nans == 0:
            print (f"{filename}.{index}: OK")
        else:
            if posinfs > 0:
                print (f"{filename}.{index}: {len(posinfs)} positive infinities detected")
            if neginfs > 0:
                print (f"{filename}.{index}: {len(neginfs)} negative infinities detected")
            if len(nans) > 0:
                print (f"{filename}.{index}: {len(nans)} not-a-numbers detected")

def handle_data(data):
    posinfs_total = 0
    neginfs_total = 0
    nans_total = 0
    for row in data:
        posinfs, neginfs, nans = handle_row(row)
        posinfs_total += posinfs
        neginfs_total += neginfs
        nans_total += nans
    return posinfs_total, neginfs_total, nans_total

def handle_row(row):
    posinfs_total = 0
    neginfs_total = 0
    nans_total = 0
    for cell in row:
        posinfs, neginfs, nans = handle_cell(cell)
        posinfs_total += posinfs
        neginfs_total += neginfs
        nans_total += nans
    return posinfs_total, neginfs_total, nans_total


def handle_cell(cell):
    posinfs = numpy.argwhere(numpy.isposinf(cell))
    neginfs = numpy.argwhere(numpy.isneginf(cell))
    nans = numpy.argwhere(numpy.isnan(cell))

    return (len(posinfs), len(neginfs), len(nans))

if __name__ == '__main__':
    main()