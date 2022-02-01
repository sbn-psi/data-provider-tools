#!/usr/bin/env python3
'''
Go through an uncompressed PDF file and remove vector strokes that are ouside of 16-bit int range,
as required by PDF/A
'''

import argparse
import sys
import re

def main():
    '''
    Get the arguments, and handle input and output.
    '''

    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args()

    with open(args.input, "rb") as infile, open(args.output, "wb") as outfile:
        for line in infile:
            outfile.write(filter(line))

def filter(line:bytes):
    '''
    Determine if a line has a stroke that is out of range, and replace it with blanks if so.
    '''
    linestr = line.decode('UTF-8', errors='ignore')
    if re.match('-?\d+.\d+ -?\d+.\d+ l', linestr):
        floats = [float(x) for x in linestr.split()[:-1]]
        if any(x < -32768 or x > 32767 for x in floats):
            return (' ' * (len(line) - 1) + '\n').encode('UTF-8')
    return line

if __name__ == '__main__':
    sys.exit(main())
