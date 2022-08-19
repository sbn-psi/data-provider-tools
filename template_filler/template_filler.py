#!/usr/bin/env python3

import csv
import re
import sys
import argparse
import jinja2
import os.path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--template-file", help="The path to the template file used to generate the labels", required=True)
    parser.add_argument("--csv-file", help="The path to the CSV file that will supply values for the templates", required=True)
    parser.add_argument("--output-path", help="The directory where the generated labels will go.", required=True)
    args = parser.parse_args()

    template_filename = os.path.basename(args.template_file)
    specified_template_directory = os.path.dirname(args.template_file)
    template_directory = specified_template_directory if os.path.isabs(specified_template_directory) else os.path.join(".", specified_template_directory)
    template_loader = jinja2.FileSystemLoader(template_directory)
    environment = jinja2.Environment(loader=template_loader, autoescape=jinja2.select_autoescape())
    template = environment.get_template(template_filename)

    with open(args.csv_file) as f:
        for d in csv.DictReader(f):
            with open(os.path.join(args.output_path, d["filename"]), "w") as outfile:
                outfile.write(template.render(d))

if __name__ == '__main__':
    sys.exit(main())