import sys
import os

def main():
    path = sys.argv[1]
    images = [f for f in (os.listdir(path)) if f.endswith(".png")]

    print "<head></head>"

    print "<body>"
    print "<h1>Title goes here</h1>"
    print "<p>Publication date goes here</p>"
    print "<h2>Introduction</h2>"
    print "<p>Intro text goes here</p>"

    print "<h2>Table of Images</h2>"
    print "<a id='toc'/>"
    for i in images:
        base = i.replace('.png', '')
        print "<div><a href='#%s'>%s</a></div>" % (i,base)

    for i in images:
        base = i.replace('.png', '')
        print "<div style='page-break-before:always'><a id='%s'/><h2>%s</h2><img src='%s'/></div>" % (i,base,i)
    print "</body>"

if __name__ == "__main__":
    main()
