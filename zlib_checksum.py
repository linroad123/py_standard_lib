#!/usr/bin/python

import zlib

data = open('zip_memory.py','r').read()

cksum = zlib.adler32(bytes(data,'utf-8'))
print('Adler32 : %12d' % cksum)
print('         %12d' % zlib.adler32(bytes(data,'utf-8'),cksum))

cksum = zlib.crc32(bytes(data,'utf-8'))
print('CRC-32 : %12d' % cksum)
print('         %12d' % zlib.crc32(bytes(data,'utf-8'),cksum))