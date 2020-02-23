# -*- coding: utf-8 -*-
import constants as constants
import schemas


class Document:
    
    def __init__(self,pub_dir, header=constants.header):
        self.content = ""
        self.pub_dir=pub_dir
        self.header=header
        self.drink_print_order = [
            {'key':'name',     'desc':'Öl namn',        'p':'+','ind':2,'fn':self.string_writer},
            {'key':'desc',     'desc':'Beskrivning',    'p':'+','ind':2,'fn':self.string_writer},
            {'key':'country',  'desc':'Land/Länder',    'p':'+','ind':2,'fn':self.string_writer},
            {'key':'brewery',  'desc':'Bryggeri(er)',   'p':'+','ind':2,'fn':self.string_writer},
            {'key':'links',    'desc':'Länk(ar)',       'p':'+','ind':2,'fn':self.string_writer},
            {'key':'brewer',   'desc':'Bryggare',       'p':'+','ind':2,'fn':self.string_writer},
            {'key':'type_nr',  'desc':'Öltyp',          'p':'+','ind':2,'fn':self.type_writer},
            {'key':'type_desc','desc':'Öltyp (fritext)','p':'+','ind':2,'fn':self.string_writer},
            {'key':'abv',      'desc':'ABV',            'p':'+','ind':2,'fn':self.string_writer},
            {'key':'abw',      'desc':'ABW',            'p':'+','ind':2,'fn':self.string_writer},
            {'key':'ibu',      'desc':'IBU',            'p':'+','ind':2,'fn':self.string_writer},
            {'key':'reviews',  'desc':'Provning(ar)',   'p':'+','ind':2,'fn':self.reviews_writer}]

        self.review_order = [
            {'key':'date',       'desc':'Datum',                            'p':'+','ind':4, 'fn':self.string_writer},
            {'key':'group',      'desc':'Provare',                          'p':'+','ind':6, 'fn':self.string_writer},
            {'key':'place',      'desc':'Plats',                            'p':'+','ind':6, 'fn':self.string_writer},
            {'key':'count',      'desc':'Antal provare',                    'p':'+','ind':6, 'fn':self.string_writer},
            {'key':'review_type','desc':'Öltyp (snittbetyg)',               'p':'+','ind':6, 'fn':self.string_writer},
            {'key':'review_over','desc':'Personlig bedömning (snittbetyg)', 'p':'+','ind':6, 'fn':self.string_writer},
            {'key':'review_uniq','desc':'Unik och Intressant (snittbetyg)', 'p':'+','ind':6, 'fn':self.string_writer},
            {'key':'comments',   'desc':'Kommentar(er)',                    'p':'+','ind':8, 'fn':self.string_writer}]
        
    def reviews_writer(self, reviews, name,_,__):
        self.content+="***** {}\n".format(name.encode("utf-8"))
        for review in reviews:
            for d in self.review_order:
                ind=d['ind']
                key=d["key"]
                desc=d["desc"]
                print_function=d["fn"]
                p=d["p"]
                if key in review:
                    print_function(review[key], desc,ind,p)

    def type_writer(self, desc, name, indent,p):
        self.content+= " "*indent+ p +" {}: {} - {}\n".format(str(name),str(desc).encode("utf-8"),constants.type_constants[desc])
                    
    def string_writer(self, desc, name, indent,p):
        if isinstance(desc,unicode):
            self.content+= " "*indent+ p+" {}: {}\n".format(str(name),str(desc.encode("utf-8")))            
        elif isinstance(desc, str) or isinstance(desc, int) or isinstance(desc,float):
            self.content+= " "*indent+ p+" {}: {}\n".format(str(name),str(desc).encode("utf-8"))
        elif isinstance (desc,list):
            if len(desc)==1:
                self.content+=" "*indent+ p+" {}: {}\n".format(str(name),str(desc[0].encode("utf-8")))
            else:
                self.content+=" "*indent+p+" {}:\n".format(str(name))
                # p={"+":"-","-":"*","*":"-"}[p]
                for d in desc:
                    self.content+=" "*(indent+4) +p+" {}\n".format(str(d.encode("utf-8")))

                    
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
            ind=d["ind"]
            print_function=d["fn"]
            p=d["p"]
            if key in doc:
                print_function(doc[key],desc,ind,p)

    def print_drink_reviews(self,doc):
        for drink in doc:
            self.content+= "**** {}\n".format(drink["name"].encode("utf-8"))
            self.print_rest_of_drink(drink)

    def create_content(self,print_dict):
        """# print_dict = {"country": {"brewery":[{drink_name:doc}]}}
        """
        self.content += "* Drycker och provningar\n"

        for brewery in self.print_country_get_breweries(print_dict):
            for drinks in self.print_brewery_get_drinks(brewery):
                self.print_drink_reviews(drinks)

    def save_basic_file(self,file):
        save_content=self.header+"\n"+self.content
        save_file = self.pub_dir+file
        with open(save_file,"w+") as s:
            s.write(save_content)
        print("Saved save_file:{}".format(save_file))
