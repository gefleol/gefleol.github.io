#-*- coding: utf-8 -*-
import yaml
import codecs

def get_drink_dict(drink_file):
    """Get a dict from yaml-file
    """
    with codecs.open(drink_file, 'rb', encoding='utf-8') as s:
        stream=s.read()
        return yaml.load(stream,Loader=yaml.FullLoader)

def order_drinks(unorderd_drinks):
    """order a list of drinks in a dict. [drink1, drink2,...] -> 

    {country_1:{brewery_1:drink1, brewery_2:drink2}, country_2:{brewery_n:drink3}}
    
    """
    print_dict=dict()
    for doc in unorderd_drinks:
        country=doc["country"][0]
        brewery=doc["brewery"][0]
        if country not in print_dict:
            print_dict[country]=dict()
        if brewery not in print_dict[country]:
            print_dict[country][brewery]=[]
        print_dict[country][brewery].append(doc)
    return print_dict

