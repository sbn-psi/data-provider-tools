#!/usr/bin/env python3

import sys
import argparse
import csv

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("basefile", help="The file to merge onto")
    parser.add_argument("addfile", help="The file to merge from")
    parser.add_argument("result", help="The that will hold the result")
    args = parser.parse_args()

    basedicts = csvToDicts(args.basefile)

    mergedicts = csvToDicts(args.addfile)

    if basedicts and mergedicts:
        basekeycol = list(basedicts[0].keys())[0]
        mergekeycol = list(mergedicts[0].keys())[0]

        indexed = indexDicts(csvToDicts(args.addfile), mergekeycol)

        for d in basedicts:
            key = d[basekeycol]
            if key in indexed:
                d.update(indexed[key])

        dictsToCsv(args.result, basedicts)


'''
Convert a list of dictionaries to a dictionary of dictionaries,
with the value of the specified key as the new key.
'''
def indexDicts(dicts, column):
    result = {}
    for d in dicts:
        result[d[column]] = d
    return result


'''
Convert a CSV file to a list of dictionaries
'''
def csvToDicts(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return [x for x in reader]


'''
Convert a list of dictionaries to a CSV file.
'''
def dictsToCsv(filename, dicts):
    with open(filename, "w") as f:
        writer = csv.DictWriter(f, dicts[0].keys())
        writer.writeheader()
        writer.writerows(dicts)



if __name__ == "__main__":
    sys.exit(main())
