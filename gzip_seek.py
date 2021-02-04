#!/usr/bin/python

import gzip
with gzip.open('example.text.gz','rb') as input_file:
    print('Enter file:')
    all_data = input_file.read()
    print(all_data)

    expected = all_data[5:15]
    input_file.seek(0)
    input_file.seek(5)
    print('Starting at position 5 for 10 bytes:')
    partial = input_file.read(10)
    print(partial)

    print(expected == partial)
