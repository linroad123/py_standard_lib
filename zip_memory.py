#!/usr/bin/python

import zlib
import binascii

original_data = 'this is original text.'
print('original : ',len(original_data),original_data)

compressed = zlib.compress(original_data.encode())
print('compressed : ',len(compressed),binascii.hexlify(compressed))

decompressed = zlib.decompress(compressed)
print('Decompressed : ',len(decompressed),decompressed)