#!/usr/bin/env python3

import csv
from dataclasses import replace
import sys
import argparse
import jinja2
import os.path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template-file", help="The path to the template file used to generate the labels", required=True)
    parser.add_argument("--csv-file", help="The path to the CSV file that will supply values for the templates", required=True)
    parser.add_argument("--output-path", help="The directory where the generated labels will go.", required=True)
    parser.add_argument("--filename-column", help="The column in the CSV file that specifies the label file name", default="filename")
    parser.add_argument("--product-id-column", help="The column in the CSV file that specifies the product id portion of the LID", default="productId")
    parser.add_argument("--data-file-column", help="The column in the CSV file that specifies the data file name", default="dataFile")
    args = parser.parse_args()

    template_filename = os.path.basename(args.template_file)
    template_directory = os.path.realpath(os.path.dirname(args.template_file))
    template_loader = jinja2.FileSystemLoader(template_directory)
    environment = jinja2.Environment(loader=template_loader, autoescape=jinja2.select_autoescape())
    template = environment.get_template(template_filename)
    filenameColumn = "filename"
    productIdColumn = "productId"
    dataFileColumn = "dataFile"

    with open(args.csv_file) as f:
        for d in csv.DictReader(f):
            d2 = postProcess(d, filenameColumn, productIdColumn, dataFileColumn)
            with open(os.path.join(args.output_path, d[filenameColumn]), "w") as outfile:
                outfile.write(template.render(d))

def postProcess(d, filenameColumn, productIdColumn, dataFileColumn):
    if filenameColumn not in d:
        d[filenameColumn] = str.replace(d[dataFileColumn], ".fit", ".xml")
    if productIdColumn not in d:
        d[productIdColumn] = str.replace(d[dataFileColumn], ".", "_")
    return d

if __name__ == '__main__':
    sys.exit(main())