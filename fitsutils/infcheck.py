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
        pass #print (f"{filename}.{index}: Not an image")
    else:
        posinfs = len(numpy.argwhere(numpy.isposinf(data)))
        neginfs = len(numpy.argwhere(numpy.isneginf(data)))
        nans = len(numpy.argwhere(numpy.isnan(data)))
        show_result(filename, index, posinfs, neginfs, nans)

def show_result(filename, index, posinfs, neginfs, nans):
    context = f"{filename}::{index}"
    if posinfs == 0 and neginfs == 0 and nans == 0:
        print (f"{context}: OK")
    else:
        if posinfs > 0:
            print (f"{context}: {len(posinfs)} positive infinities detected")
        if neginfs > 0:
            print (f"{context}: {len(neginfs)} negative infinities detected")
        if len(nans) > 0:
            print (f"{context}: {len(nans)} not-a-numbers detected")

    
def process_table(hdu, filename, index):
    data = hdu.data
    if data is None:
        print (f"{filename}.{index}: Not a table")
    else:
        posinfs, neginfs, nans = handle_data(data)
        show_result(filename, index, posinfs, neginfs, nans)

def handle_data(data):
    stats = [handle_row(row) for row in data]
    zstats = list(zip(*stats))
    return [sum(x) for x in zstats]

def handle_row(row):
    stats = [handle_cell(cell) for cell in row]
    zstats = list(zip(*stats))
    return [sum(x) for x in zstats]

def handle_cell(cell):
    posinfs = numpy.argwhere(numpy.isposinf(cell))
    neginfs = numpy.argwhere(numpy.isneginf(cell))
    nans = numpy.argwhere(numpy.isnan(cell))

    return (len(posinfs), len(neginfs), len(nans))

if __name__ == '__main__':
    main()