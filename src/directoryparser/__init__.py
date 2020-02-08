#-*- coding: utf-8 -*-
import os

def get_drink_files(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file[-5:] == ".yaml":
                yield "{}/{}".format(root,file) 
