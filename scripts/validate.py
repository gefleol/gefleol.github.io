#-*- coding: utf-8 -*-
from schema import Schema, And, Regex, Optional
import yaml

if __name__ == '__main__':

    drink_schema = Schema({'name': And(str,len),
                      Optional('country'):And(str,len),
                      Optional('brewery'):And(str,len),
                      Optional('brewer'):And(str,len),
                      Optional('type'):And(str,len),
                      Optional('abv'):And(float,lambda n:0 <= n <=100),
                      Optional('abw'):And(float,lambda n:0 <= n <=100),
                      Optional('ibu'):float,
                      Optional('reviews'):
                     [{'date': Regex('^\d{4}-\d{2}-\d{2}'),
                       Optional('group'):And(str,len),
                       Optional('place'):And(str,len),
                       'count':int, 
                       Optional('review_type'):And(float,lambda n:0 <= n <=10), 
                       Optional('review_over'):And(float,lambda n:0 <= n <=10),
                       Optional('review_uniq'):And(float,lambda n:0 <= n <=10),
                       Optional('comments'):[str]}]})

    document="""name: "Odd Island Brew"
country: "Sverige"
brewery: "Hazie Dizzie"
type: "Ale"
abv: 6.2
reviews: 
    - date: "2020-01-02"
      group: "Gefle Olsellskap"
      place: "Terrassen"
      count: 5
      review_type: 8.3 
      comments:
        - God ol/Smakvik"""
    print drink_schema.validate(yaml.load(document))
