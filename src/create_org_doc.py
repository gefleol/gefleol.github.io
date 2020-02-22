import directoryparser as dir
import drinks_parser as dp
from document.document import Document
from document.constants import *

drink_directory = "../data/drinks/"
pub_directory = "../pub/"
print_dict=dict()
docs=[]

if __name__ == '__main__':   
    for drink_file in dir.get_drink_files(drink_directory):
        docs.append(dp.get_drink_dict(drink_file))

    # To make headlines country->brewery->drinks->review where
    # country, brewery, drink is uniqe:
    # {"country": {"brewery":[{drink_name:doc}]}}
    print_dict=dp.order_drinks(docs)

    main_file=Document(pub_directory, js_header)
    main_file.create_content(print_dict)
    main_file.save_basic_file("provningar_main.org")


    one_file=Document(pub_directory, header)
    one_file.create_content(print_dict)
    one_file.save_basic_file("provningar_en_fil.org")

