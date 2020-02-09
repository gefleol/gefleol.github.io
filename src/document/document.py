import header_constants as constants
class Document:
    def __init__(self,pub_dir):
        self.content = ""
        self.pub_dir=pub_dir

        
    def create_content(self,print_dict):
        """# print_dict = {"country": {"brewery":[{drink_name:doc}]}}
        """
        for country in print_dict.keys():
            self.content+="** {}\n".format(country.encode("utf-8"))
            for brewery in print_dict[country]:
                self.content+="*** {}\n".format(brewery.encode("utf-8"))
                for drink in print_dict[country][brewery]:
                    self.content+="**** {}\n".format(drink["name"].encode("utf-8"))
                    for review in drink["reviews"]:
                        self.content+="    + Provdatum: {}\n".format(review["date"])

    def save_basic_file(self,file):
        save_content=constants.header+"\n"+self.content
        save_file = self.pub_dir+file
        with open(save_file,"w+") as s:
            s.write(save_content)
        print("Saved save_file:{}".format(save_file))
