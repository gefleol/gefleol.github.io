#-*- coding: utf-8 -*-
from schema import Schema, And, Regex, Optional
import yaml
import codecs

if __name__ == '__main__':

    drink_json_schema = {'name': And(Regex('\w+'),len),
                      Optional('country'):And(Regex('\w+'),len),
                      Optional('brewery'):And(Regex('\w+'),len),
                      Optional('brewer'):And(Regex('\w+'),len),
                      Optional('type'):And(Regex('\w+'),len),
                      Optional('abv'):And(float,lambda n:0 <= n <=100),
                      Optional('abw'):And(float,lambda n:0 <= n <=100),
                      Optional('ibu'):float,
                      Optional('reviews'):
                         [{'date': Regex('^\d{4}-\d{2}-\d{2}'),
                           Optional('group'):And(Regex('\w+'),len),
                           Optional('place'):And(Regex('\w+'),len),
                           'count':int, 
                           Optional('review_type'):And(float,lambda n:0 <= n <=10), 
                           Optional('review_over'):And(float,lambda n:0 <= n <=10),
                           Optional('review_uniq'):And(float,lambda n:0 <= n <=10),
                           Optional('comments'):[Regex('\w+')]}]}

    drink_schema=Schema(drink_json_schema)
    with codecs.open('../data/drinks/odd_island_brew-hazie_dizzie.yaml', 'rb', encoding='utf-8') as s:
        stream=s.read()
        document=yaml.load(stream,Loader=yaml.FullLoader)
        drink_schema.validate(document)
