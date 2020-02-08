import directoryparser as dir
import drinks_parser as dp


drink_directory="/home/johan/dev/gefleol.github.io/data/drinks/"
org_content=""
print_dict=dict()
docs=[]

if __name__ == '__main__':            
    for drink_file in dir.get_drink_files(drink_directory):
        docs.append(dp.get_drink_dict(drink_file))

# {"country": {"brewery":[{drink_name:doc}]}}
    print_dict=dp.order_drinks(docs)
        
    for country in print_dict.keys():
        org_content+="** {}\n".format(country.encode("utf-8"))
        for brewery in print_dict[country]:
            org_content+="*** {}\n".format(brewery.encode("utf-8"))
            for drink in print_dict[country][brewery]:
                org_content+="**** {}\n".format(drink["name"].encode("utf-8"))
                for review in drink["reviews"]:
                    org_content+="    + Provdatum: {}\n".format(review["date"])
                    # org_content+="        - Land: {}\n".format(re)
    print org_content
            
    
