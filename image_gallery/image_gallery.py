#! /usr/bin/env python

import sys
import os
import os.path

def print_header(outfile):
    outfile.write("<head></head>\n")

    outfile.write("<body>\n")
    outfile.write("<h1>Title goes here</h1>\n")
    outfile.write("<p>Publication date goes here</p>\n")
    outfile.write("<h2>Introduction</h2>\n")
    outfile.write("<p>Intro text goes here</p>\n")


def print_toc(outfile, images):
    outfile.write("<h2>Table of Images</h2>\n")
    outfile.write("<a id='toc'/>\n")
    for i in images:
        base = i.replace('.png', '')
        outfile.write("<div><a href='#%s'>%s</a></div>\n" % (i,base))

def print_gallery(outfile, images):
    for i in images:
        base = i.replace('.png', '')
        outfile.write("<div style='page-break-before:always'><a id='%s'/><h2>%s</h2><img src='%s'/></div>\n" % (i,base,i))


def print_footer(outfile):
    outfile.write("</body>\n")


def main():
    path = sys.argv[1]
    outfilename = sys.argv[2]
    images = [f for f in (os.listdir(path)) if f.endswith(".png")]
    
    with open(os.path.join(path, outfilename), 'w') as outfile:
      print_header(outfile)
      print_toc(outfile, images)
      print_gallery(outfile, images)
      print_footer(outfile)



if __name__ == "__main__":
    main()
