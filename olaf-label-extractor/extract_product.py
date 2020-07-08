#! /usr/bin/env python3
'''
Extracts metadata from a series of PDS 4 labels for reuse in OLAF.
'''

import sys
from bs4 import BeautifulSoup

FIELDS = [
    "File Name",
    "Author List",
    "Product Name",
    "Observing System Bookmark",
    "Target Name",
    "Target Type",
    "Start Time",
    "Product Description",
    "Stop Time",
    "Product Processing Level",
    "Product Wavelength Ranges",
    "Science Search Facet",
    "Reference Key"
]

INST_TYPES = ['Instrument', 'Literature Search']

def main(argv=None):
    '''
    Entry point into the program. Takes the name of a PDS4 label file
    and an output CSV filename.
    '''
    if argv is None:
        argv = sys.argv

    infilenames = argv[1:-1]
    outfilename = argv[-1]

    datas = [translate_filename(filename) for filename in infilenames]
    output = "\r\n".join(datas) + "\r\n"
    print(output)

    with open(outfilename, 'w') as outfile:
        outfile.write(output)

def translate_filename(infilename):
    '''
    Translate a file with the given name into a product index line.
    '''
    with open(infilename) as infile:
        return translate_file(infile)


def translate_file(infile):
    '''
    Translate a file into a product index line
    '''
    soup = BeautifulSoup(infile, 'lxml-xml')
    return format_product(extract(soup), FIELDS)

def extract(soup):
    '''
    Converts a parsed xml document into a flattened object
    '''
    identification_area = soup.find("Identification_Area")
    file_element = soup.find("File_Area_Observational").File
    citation_information = soup.find("Citation_Information")
    obs_components = soup.find_all("Observing_System_Component")
    target_identification = soup.find("Target_Identification")
    time_coordinates = soup.find("Time_Coordinates")
    primary_result_summary = soup.find("Primary_Result_Summary")
    wavelength_range = primary_result_summary.find_all("wavelength_range")
    facets = primary_result_summary.find_all("Science_Facets")
    reference_keys = soup.find_all("External_Reference")

    return {
        "File Name": file_element.file_name.string,
        "Author List": citation_information.author_list.string,
        "Product Name": identification_area.title.string,
        "Product Processing Level": primary_result_summary.processing_level.string,
        "Product Wavelength Ranges": ",".join(x.string for x in wavelength_range),
        "Science Search Facet": ",".join(x.facet1.string for x in facets),
        "Observing System Bookmark": "Obs." + ";".join(osc_name(x) for x in obs_components),
        "Target Name": target_identification.find("name").string,
        "Target Type": target_identification.type.string,
        "Start Time": time_coordinates.start_date_time.string,
        "Stop Time": time_coordinates.stop_date_time.string,
        "Product Description": citation_information.description.string.replace("\n", ""),
        "Reference Key": ",".join(x.reference_text.string for x in reference_keys)
    }

def osc_name(osc):
    '''
    Gets the name of an observing system component, and normalizes it
    '''
    return ",".join([osc.find("name").string.replace(" ", "")])


def format_product(product, keyspec):
    '''
    Formats a flatteneed product object into a csv line
    '''
    return ",".join('"' + str(product[key]) + '"' for key in keyspec)

if __name__ == "__main__":
    sys.exit(main())
