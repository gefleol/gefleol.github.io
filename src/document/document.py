# -*- coding: utf-8 -*-
import constants as constants
import schemas




class Document:


    
    def __init__(self,pub_dir):
        self.content = ""
        self.pub_dir=pub_dir
        self.drink_print_order = [{'key':'desc','desc':'Beskrivning','fn':self.string_writer},
                             {'key':'country','desc':'Land/Länder','fn':self.string_writer},
                             {'key':'brewery','desc':'Bryggeri(er)','fn':self.string_writer},
                             {'key':'links','desc':'Länk(ar)','fn':self.string_writer},
                             {'key':'brewer','desc':'Bryggare','fn':self.string_writer},
                             {'key':'type_nr','desc':'Öltyp','fn':self.string_writer},
                             {'key':'type_desc','desc':'Öltyp (fritext)','fn':self.string_writer},
                             {'key':'abv','desc':'ABV','fn':self.string_writer},
                             {'key':'abw','desc':'ABW','fn':self.string_writer},
                             {'key':'ibu','desc':'IBU','fn':self.string_writer}]



    def string_writer(self, desc, name):
        print "- {}: {}\n".format(str(name),str(desc).encode("utf-8"))
        
    def print_country_get_breweries(self, doc):
        for country in doc.keys():
            self.content+="** {}\n".format(country.encode("utf-8"))
            yield doc[country]

    def print_brewery_get_drinks(self,doc):
        for brewery in doc.keys():
            self.content+="*** {}\n".format(brewery.encode("utf-8"))
            yield doc[brewery]

    def print_rest_of_drink(self, doc):
        for d in self.drink_print_order:
            key=d["key"]
            desc=d["desc"]
            print_function=d["fn"]
            if key in doc:
                print_function(doc[key],desc)
            
    def print_drink_get_reviews(self,doc):
        for drink in doc:
            self.content+= "**** {}\n".format(drink["name"].encode("utf-8"))
            self.print_rest_of_drink(doc)
            
            
            
    def create_content(self,print_dict):
        """# print_dict = {"country": {"brewery":[{drink_name:doc}]}}
        """
        for brewery in self.print_country_get_breweries(print_dict):
            for drink in self.print_brewery_get_drinks(brewery):
                for review in self.print_drink_get_reviews(drink):
                    pass
                    # self.content+="**** {}\n".format(drink["name"].encode("utf-8"))
                    # for review in drink["reviews"]:
                    #     self.content+="    + Provdatum: {}\n".format(review["date"])

    def save_basic_file(self,file):
        save_content=constants.header+"\n"+self.content
        save_file = self.pub_dir+file
        with open(save_file,"w+") as s:
            s.write(save_content)
        print("Saved save_file:{}".format(save_file))
