#!/usr/bin/python

import hashlib
from hashlib_data import lorem

h5 = hashlib.md5()
h5.update(lorem.encode())
h1 = hashlib.sha1()
h1.update(lorem.encode())

print(h5.hexdigest)
print(h1.hexdigest)

h = hashlib.md5()
h.update(lorem.encode())
all_at_once = h.hexdigest()

def chunkize (size,text):
    "Return parts of the text in size-based increments."
    start = 0
    while start < len(text):
        chunk = text[start:start+size]
        yield chunk
        start +=size
        return


h = hashlib.md5()
for chunk in chunkize(64,lorem):
    h.update(chunk.encode())
line_by_line = h.hexdigest()
print('All at once : ', all_at_once)
print('Line by Line :',line_by_line)
print('Same:    ',(all_at_once==line_by_line))