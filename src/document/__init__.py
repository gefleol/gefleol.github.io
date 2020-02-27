# -*- coding: utf-8 -*-

import os
import uuid

def insert(originalfile,string):
    with open(originalfile,'r') as f:
        with open('newfile.txt','w') as f2: 
            f2.write(string)
            f2.write(f.read())
    os.rename('newfile.txt',originalfile)

def get_uuid():
    return str(uuid.uuid1())
