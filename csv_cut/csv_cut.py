#!/usr/bin/env python3

import sys
import argparse
import csv

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("csvfile", help="The file to remove columns from")
    parser.add_argument("resultfile", help="The file to hold the results")
    parser.add_argument("columns", help="The columns to remove", nargs="+")
    args = parser.parse_args()

    with open(args.csvfile) as fin:
        reader = csv.DictReader(fin)
        newColumns = [x for x in reader.fieldnames if x not in args.columns]
        dicts = ({k: row[k] for k in newColumns} for row in reader)

        with open(args.resultfile, "w") as fout:
            writer = csv.DictWriter(fout, newColumns)
            writer.writeheader()
            writer.writerows(dicts)



if __name__ == '__main__':
    sys.exit(main())