import directoryparser as dir
import document as doc
import drinks_parser as dp
drink_directory="/home/johan/dev/gefleol.github.io/data/drinks/"
for drink_file in dir.get_drink_files(drink_directory):
    if not "uuid" in dp.get_drink_dict(drink_file).keys():
        doc.insert(drink_file,"uuid: '{}'\n".format(doc.get_uuid()))
        print str(drink_file)
print("uuid_prepending - klar.")
