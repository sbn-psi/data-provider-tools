#!/usr/bin/env python3

import csv
import sys
import argparse
import jinja2
import os.path

def main():
    args = getArgs()
    template = loadTemplate(args.template_file)
    generateLabels(args.csv_file, template, args.output_path, args.filename_column, args.product_id_column, args.data_file_column)

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template-file", help="The path to the template file used to generate the labels", required=True)
    parser.add_argument("--csv-file", help="The path to the CSV file that will supply values for the templates", required=True)
    parser.add_argument("--output-path", help="The directory where the generated labels will go.", required=True)
    parser.add_argument("--filename-column", help="The column in the CSV file that specifies the label file name", default="filename")
    parser.add_argument("--product-id-column", help="The column in the CSV file that specifies the product id portion of the LID", default="productId")
    parser.add_argument("--data-file-column", help="The column in the CSV file that specifies the data file name", default="dataFile")
    return parser.parse_args()


def loadTemplate(template_file):
    template_filename = os.path.basename(template_file)
    template_directory = os.path.realpath(os.path.dirname(template_file))
    template_loader = jinja2.FileSystemLoader(template_directory)
    environment = jinja2.Environment(loader=template_loader, autoescape=jinja2.select_autoescape())
    return environment.get_template(template_filename)

def generateLabels(csv_file, template, output_path, filenameColumn, productIdColumn, dataFileColumn):
    with open(csv_file) as f:
        for d in csv.DictReader(f):
            d2 = postProcess(d, filenameColumn, productIdColumn, dataFileColumn)
            generateLabel(d2, output_path, filenameColumn, template)

def generateLabel(d2, output_path, filenameColumn, template):
    with open(os.path.join(output_path, d2[filenameColumn]), "w") as outfile:
        outfile.write(template.render(d2))

def postProcess(d, filenameColumn, productIdColumn, dataFileColumn):
    if filenameColumn not in d:
        root, ext = os.path.splitext(d[dataFileColumn])
        d[filenameColumn] = root + ".xml"
    if productIdColumn not in d:
        d[productIdColumn] = str.replace(d[dataFileColumn], ".", "_")
    return d

if __name__ == '__main__':
    sys.exit(main())