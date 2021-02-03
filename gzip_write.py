#!/usr/bin/python

import gzip
import os

outfilename = 'example.text.gz'
with gzip.open(outfilename,'wb') as output:
    string = 'Contents of the example file go here.\n'
    output.write(string.encode())

print (outfilename,'contains',os.stat(outfilename).st_size,'bytes')
os.system('file -b --mime %s' % outfilename)

