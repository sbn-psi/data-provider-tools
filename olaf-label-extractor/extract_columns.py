#! /usr/bin/env python3
'''
Extracts the column information from a PDS4 product and converts it into an
OLAF column information file.
'''

import re
import sys
from bs4 import BeautifulSoup

DATA_TYPES = {
    'ASCII_Integer': 'integer',
    'ASCII_Real': 'real',
    'ASCII_String': 'string',
    'UTF8_String': 'string',
    'ASCII_Date_Time_YMD': 'datetime',
    'ASCII_Date_YMD': 'date'
}

FORMATS = {
    'd': 'I',
    'f': 'F',
    's': 'A',
    'e': 'E'
}

FW_LINES = ['name', 'data_type', 'units', 'missing_constant', 'description', 'format']
CSV_LINES = ['name', 'data_type', 'units', 'missing_constant', 'description']

def main(argv=None):
    '''
    Entry point into the program. Takes the name of a PDS4 label file
    and an output CSV filename.
    '''
    if argv is None:
        argv = sys.argv

    infilename = argv[1]
    outfilename = argv[2]

    with open(infilename) as infile:
        contents = translate_file(infile)

    with open(outfilename, 'w') as outfile:
        outfile.write(contents)

def translate_file(infile):
    '''
    Translate a PDS4 label into a column definition file for use with OLAF.
    '''
    soup = BeautifulSoup(infile, 'lxml-xml')

    if soup.find('Table_Character'):
        return translate_table(soup.find('Table_Character'), 'Field_Character', FW_LINES)

    if soup.find('Table_Delimited'):
        return translate_table(soup.find('Table_Delimited'), 'Field_Delimited', CSV_LINES)

    return 'Unrecognized table.'

def translate_table(table, field_spec, linespec):
    '''
    Translates a single table within the label into a column definition file.
    '''
    fields = [translate(extract(field)) for field in table.find_all(field_spec)]
    output_lines = [format_line(fields, k) for k in linespec]
    contents = '\r\n'.join(output_lines) + '\r\n'
    return contents

def extract(field):
    '''
    Extract the field information from a single PDS4 field.
    '''
    return {
        'name': field.find('name').string,
        'description': field.description.string,
        'data_type': field.data_type.string,
        'units': field.unit.string if field.unit else '',
        'missing_constant':
            field.Special_Constants.missing_constant.string if field.Special_Constants else '',
        'format': field.field_format.string if field.field_format else ''
    }

def translate(field):
    '''
    Convert some of the field values into someting that OLAF expects.
    '''
    return {
        'name': field['name'],
        'description': field['description'].replace("\r\n", ' ').replace("\n", ' '),
        'data_type': DATA_TYPES[field['data_type']],
        'units': field['units'],
        'missing_constant': field['missing_constant'],
        'format': translate_format(field['format']) if field['format'] else ''
    }

def translate_format(format_str):
    '''
    Convert a POSIX format back into Fortran format.
    '''
    pattern = r'\%(\-?)(\d+)(\.\d*)?([defs])'
    matches = re.match(pattern, format_str)
    datatype, width, precision = matches.group(4, 2, 3)
    return ''.join([FORMATS[datatype],
                    width,
                    precision if precision else ''])

def format_line(fields, key):
    '''
    Convert a single attribute of each field into a comma separated list of values
    '''
    return ','.join(['"' + field[key] + '"' for field in fields])

if __name__ == '__main__':
    sys.exit(main())
