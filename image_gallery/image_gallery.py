import sys
import os

def print_header():
    print "<head></head>"

    print "<body>"
    print "<h1>Title goes here</h1>"
    print "<p>Publication date goes here</p>"
    print "<h2>Introduction</h2>"
    print "<p>Intro text goes here</p>"


def print_toc(images):
    print "<h2>Table of Images</h2>"
    print "<a id='toc'/>"
    for i in images:
        base = i.replace('.png', '')
        print "<div><a href='#%s'>%s</a></div>" % (i,base)

def print_gallery(images):
    for i in images:
        base = i.replace('.png', '')
        print "<div style='page-break-before:always'><a id='%s'/><h2>%s</h2><img src='%s'/></div>" % (i,base,i)


def print_footer():
    print "</body>"


def main():
    path = sys.argv[1]
    images = [f for f in (os.listdir(path)) if f.endswith(".png")]

    print_header()
    print_toc(images)
    print_gallery(images)
    print_footer()



if __name__ == "__main__":
    main()
