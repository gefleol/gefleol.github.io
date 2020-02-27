#-*- coding: utf-8 -*-
from schemas import drink_schema
import yaml
import codecs
import sys

def validate_drink_file(drink_file):
    with codecs.open(drink_file, 'rb', encoding='utf-8') as s:
        stream=s.read()
        document=yaml.load(stream,Loader=yaml.FullLoader)
        try:
            drink_schema.validate(document)
        except:
            print "Validation ERROR in file: {}".format(drink_file)
            print "ERROR: {}".format(str(sys.exc_info()))
