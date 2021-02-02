#!usr/bin/python

import zlib
import binascii

compressor = zlib.compressobj(1)

with open('zip_memory.py','r') as input :
    while True:
        block = input.read(64)
        #print(type(block))
        if not block:
            break
        compressed = compressor.compress(bytes(block, "utf8"))
        if compressed:
            print('Compressed. %s' % binascii.hexlify(compressed))
        else:
            print('buffering...')
    remaining = compressor.flush()
    print('Flushed: %s' % binascii.hexlify(remaining))