#!/usr/bin/python

import hmac
import hashlib

string = 'secret-shared-key-here'
string2 = ''
digest_maker = hmac.new(string.encode('utf-8'),string2.encode(),hashlib.sha1)

with open('hmac_sha.py','rb') as f :
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)

digest = digest_maker.hexdigest()
print(digest)