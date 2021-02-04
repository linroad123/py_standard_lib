#!usr/bin/env /usr/local/bin/python
# encoding: utf-8

import tarfile
import os
import time

start = time.time()
tar = tarfile.open('C:\\Python27\\Lib.tar','w')
for root,dir,files in os.walk('C:\\Python27\\Lib'):
    for file in files:
        fullpath = os.path.join(root,file)
        tar.add(fullpath,arcname=file)
tar.close()
print(time.time()-start)