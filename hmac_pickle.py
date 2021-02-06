#!/usr/bin/python

import hashlib
import hmac
import pickle
import pprint
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

def make_digest(message):
    string = 'secret-shared-key-here'
    string2 = ''
    hash = hmac.new(string.encode('utf-8'),string2.encode(),hashlib.sha1)
    return hash.hexdigest()

class SimpleObject(object) :
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

# mock a writable StringIO Socket or pipe
out_s = StringIO()
o = SimpleObject('digest matches')
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = '%s %s' % (digest,len(pickled_data))

print('WRITING:',header)
out_s.write(header + '\n')
out_s.write(str(pickled_data))



o = SimpleObject('digest does not match')
pickled_data = pickle.dumps(o)
digest = make_digest('not the pickled data at all')
header = '%s %s' % (digest,len(pickled_data))
print('\nWRITING:',header)
out_s.write(header + '\n')
out_s.write(str(pickled_data))
out_s.flush()



in_s = StringIO(out_s.getvalue())
while True:
    first_line = in_s.readline()
    if not first_line :
        break
    incoming_digest,incoming_length = first_line.split(' ')
    incoming_length = int(incoming_length)

    print('READ:',incoming_digest,incoming_length)
    incoming_pickled_data = in_s.read(incoming_length)
    actual_digest = make_digest(incoming_pickled_data)

    print('ACTUAL:',actual_digest)

    if incoming_digest != actual_digest :
        print('WRANING: Data corruption')
    else:
        obj = pickle.loads(bytes(incoming_pickled_data,encoding='utf-8'))
        print('OK:',obj)