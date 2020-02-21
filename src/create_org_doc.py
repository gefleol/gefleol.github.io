import directoryparser as dir
import drinks_parser as dp
from document.document import Document

drink_directory = "../data/drinks/"
pub_directory = "../pub/"
print_dict=dict()
docs=[]

if __name__ == '__main__':            
    for drink_file in dir.get_drink_files(drink_directory):
        docs.append(dp.get_drink_dict(drink_file))

    # {"country": {"brewery":[{drink_name:doc}]}}
    print_dict=dp.order_drinks(docs)
    doc=Document(pub_directory)
    doc.create_content(print_dict)
    doc.save_basic_file("test.org")
    
