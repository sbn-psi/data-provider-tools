#! /usr/bin/env python3
import sys

import jinja2

FORMS = {
    '1I': {'bytes':2, 'type':'SignedMSB2'},
    '1J': {'bytes':4, 'type':'SignedMSB4'},
    '1E': {'bytes':4, 'type':'IEEE754MSBSingle'},
    '1D': {'bytes':8, 'type':'IEEE754MSBDouble'}
}

FORMATS = {
    'I': '%%%id',
    'F': '%%%i.%if',
    'G': '%%%i.%if',
    'E': '%%%i.%ie'
}

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(sys.argv) < 2:
        print ('usage: table_binary.py filename')
        return 1

    filename = sys.argv[1]
    process_file(filename)

def process_file(filename):
    tablespec = extract_from_file(filename)

    template = jinja2.Template(open('template.txt').read(), trim_blocks=True, lstrip_blocks=True)
    print(template.render(tablespec))
    
def extract_from_file(filename):
    d = file_to_dict(filename)
    rows = int(d["NAXIS2"]["value"])
    rowbytes = int(d["NAXIS1"]["value"])
    cols = int(d["TFIELDS"]["value"])
    fields = get_fields(d, cols)

    return {
        "rows" : rows,
        "row_bytes": rowbytes,
        "cols": cols,
        "fields": fields
    }

def get_fields(d, cols):
    fields = [extract_field(d, str(i)) for i in range(1, cols + 1)]
    newfields = [convert_field(f) for f in fields]

    newfields[0]['position'] = 1
    for i in range(1, cols):
        newfields[i]['position'] = newfields[i-1]['position'] + int(newfields[i-1]['bytes'])
    return newfields

def convert_field(f):
    form = f['form']
    return {
        'datatype': FORMS[form]['type'],
        'bytes': FORMS[form]['bytes'],
        'format': convert_format(f['fmt']),
        'units': f['unit'],
        'name': f['name'],
        'desc': f['desc'],
        'number': f['number']
    }

def convert_format(fmt):
    format_spec = fmt[0]
    format_str = FORMATS[format_spec]
    size = extract_size(fmt)
    return format_str % (size)

def extract_size(fmt):
    size_spec = fmt[1:]
    if "." in size_spec:
        return tuple([int(x) for x in size_spec.split(".")])
    else:
        return int(size_spec)

def extract_field(d, field):
    return {
        'form' : d["TFORM" + field]["value"],
        'fmt' : d["TDISP" + field]["value"],
        'unit' : d["TUNIT" + field]["value"] if "TUNIT" + field in d else "",
        'name' : d["TTYPE" + field]["value"],
        'desc' : d["TTYPE" + field]["comment"],
        'number': field,
    }

def file_to_dict(filename):
    dicts = [line_to_dict(line) for line in open(filename)]
    return dict(
        [(d['key'], {"value": d['value'], "comment":d["comment"]}) for d in dicts]
    )


def line_to_dict(line):
    if "=" in line:
        key, value = line.split("=")
        if "/" in value:
            actual, comment = value.split("/", 1)
            return {"key": key.strip(), "value": actual.strip(" '\n"), "comment": comment.strip()}
        else:
            return {"key": key.strip(), "value": value.strip(" '\n"), "comment": ""}
    else:
        return {}


if __name__ == '__main__':
    sys.exit(main())