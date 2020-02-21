# -*- coding: utf-8 -*-
import constants as constants
import schemas




class Document:


    
    def __init__(self,pub_dir):
        self.content = ""
        self.pub_dir=pub_dir
        self.drink_print_order = [
            {'key':'name','desc':'Öl namn','fn':self.string_writer},
            {'key':'desc','desc':'Beskrivning','fn':self.string_writer},
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
        if isinstance(desc, str) or isinstance(desc, int) or isinstance(desc,float):
            self.content+= "  - {}: {}\n".format(str(name),str(desc).encode("utf-8"))
        else:
            if isinstance (desc,list):
                self.content+="  - {}: {}\n".format(str(name),str(desc[0].encode("utf-8")))
        
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
                # print "DEBUG key:{} desc:{} ".format(key,str(drink[key]))
                print_function(doc[key],desc)
            
    def print_drink_reviews(self,doc):
        print "Debug drink"+str(doc)
        for drink in doc:
            self.content+= "**** {}\n".format(drink["name"].encode("utf-8"))
            self.print_rest_of_drink(drink)
            
    def create_content(self,print_dict):
        """# print_dict = {"country": {"brewery":[{drink_name:doc}]}}
        """
        for brewery in self.print_country_get_breweries(print_dict):
            for drinks in self.print_brewery_get_drinks(brewery):
                # print ("DEBUG"+str(drink))
                self.print_drink_reviews(drinks)

    def save_basic_file(self,file):
        save_content=constants.header+"\n"+self.content
        save_file = self.pub_dir+file
        with open(save_file,"w+") as s:
            s.write(save_content)
        print("Saved save_file:{}".format(save_file))
