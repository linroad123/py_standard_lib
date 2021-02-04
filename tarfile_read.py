#!/usr/bin/python
#encoding: utf-8

import tarfile
import time

start = time.time()
t = tarfile.open('C:\\Python27\\Lib.tar','r:')
t.extractall(path = 'C:\\')
t.close()
print(time.time()-start)