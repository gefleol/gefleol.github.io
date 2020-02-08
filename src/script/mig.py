#-*- coding: utf-8 -*-
import codecs
import os
import re

def create_dir(d):
    dirname="{}/{}/".format(root_dir,d)
    directory = os.path.dirname(dirname.lower())
    if not os.path.exists(directory):
        os.makedirs(directory)

def conv_128(name):
    return re.sub(r'[^\x00-\x7F]+','_',name)
        
def create_file(land,bryggeri,namn,datum):
    file_name=(bryggeri+"--"+namn).lower().replace(" ","_")
    file_name=conv_128(file_name)+".yaml"
    full_file_name="{}/{}/{}".format(root_dir,conv_128(land),file_name)

    content=u"""name: '{}'
country:
  - '{}'
brewery:
  - '{}'
reviews:
  - date: '{}'
    group: 'Gefle Ölsellskap'
    place: 'Terrassen' 
""".format(namn.strip(),land.strip(),bryggeri.strip(),datum.strip())
    codecs.open(full_file_name.lower(),"w+",encoding="utf-8").write(content)
    
if __name__ == '__main__':
    root_dir="/home/johan/dev/gefleol.github.io/data/drinks"
    with codecs.open('/home/johan/doc/org/gos/provningar/provtillf.csv', 'rb', encoding='utf-8') as s:
        for nr,l in enumerate(s):
            file_nr,land, bryggeri,namn,datum=l.split(",")
            print str(nr)+" "+str(file_nr)
            create_dir(conv_128(land))
            create_file(land,bryggeri,namn,datum)
