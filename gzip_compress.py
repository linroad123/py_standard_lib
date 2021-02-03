#!/usr/bin/python

import gzip
import os
import hashlib

def get_hash(data):
    content = data.encode('utf-8')
    return hashlib.md5(content).hexdigest()

data = open('gzip_write.py','r').read()
cksum = get_hash(data)

print('Level    Size        Checksum')
print('-----    -------     -------------')
print('data     %10d    %s'%(len(data),cksum))

for i in range(1,10):
    filename = 'compress-leve-%s.gz' % i
    with gzip.open(filename,'wb',compresslevel=i) as output:
        output.write(data.encode())
    size = os.stat(filename).st_size
    cksum = get_hash(open(filename,'rb').read())
    print('%5d  %10d    %s' % (i,size,cksum))