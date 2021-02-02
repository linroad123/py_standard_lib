#!/usr/bin/python

import zlib
import sys
if sys.version_info < (3,):
    range = xrange
original_data = 'this is original text.'

fmt = '%15s %15s'
print(fmt % ('len(data)','len(compressed)'))
print(fmt % ('-' * 15, '-' * 15))

for i in range(5):
    data = original_data * i
    compressed = zlib.compress(data.encode())
    highlight = '*' if len(data) < len(compressed) else''
    print (fmt % (len(data),len(compressed)), highlight)