#!/usr/bin/python

import os
import tarfile

# global var
SHOW_LOG = True
# tar file location
TAR_PATH = ''
# retrieve file location dir
EXT_PATH = ''

def write_tar_file(path,content):
    with tarfile.open(path,'w') as tar:
        if SHOW_LOG:
            print('Open file: [{}]'.format(path))
        for n in content:
            if SHOW_LOG:
                print('Compressed file:[{}]'.format(path))
            tar.add(n)
        if SHOW_LOG:
            print('Close file [{}]'.format(path))
        tar.close()

def get_workspace_files():
    # obtain working dir all files, and return with list
    if SHOW_LOG:
        print('Obtain working dir all files ...')
    return os.listdir('./')

def extract_files(tar_path,ext_path,ext_name):
    '''unzip part of tar file to specific dir'''
    with tarfile.open(tar_path) as tar:
        if SHOW_LOG:
            print('Open file:[{}]'.format(tar_path))
        names = tar.getnames() 
        if SHOW_LOG:
            print('Obtain all files name:{}'.format(names))
        for name in names:
            if name.split('.')[-1] == ext_name:
                if SHOW_LOG:
                    print('extract file: [{}]'.format(name))
                tar.extract(name,path=ext_path)

def mkdir(path):
    if os.path.exists(path):
        if SHOW_LOG:
            print('exiting dir:[{}]'.format(path))
    else:
        if SHOW_LOG:
            print('making dir:[{}]'.format(path))
        os.mkdir(path)

def init():
    global SHOW_LOG
    SHOW_LOG = True

    # tar file location
    global TAR_PATH
    TAR_PATH = 'C:\\test\\hongten.tar'

    # retrieved file location
    global EXT_PATH
    EXT_PATH = 'c:\\test\\temp'

    # make dir if dir does not exit
    path = os.path.split(TAR_PATH)[0]
    mkdir(path)
    mkdir(EXT_PATH)

def main():
    init()
    content = get_workspace_files()

    write_tar_file(TAR_PATH,content)

    print('#'*50)

    extract_files(TAR_PATH,EXT_PATH,'html')

if __name__ == '__main__' :
    main()
