from schema import Schema, And, Regex, Optional

drink_json_schema = {'name': And(Regex('\w+'),len),
                     Optional('desc'):And(Regex('\w+'),len),
                     Optional('links'):[And(Regex('\w+'),len)],
                     Optional('country'):[And(Regex('\w+'),len)],
                     Optional('brewery'):[And(Regex('\w+'),len)],
                     Optional('brewer'):[And(Regex('\w+'),len)],
                     Optional('type_nr'):int,
                     Optional('type_desc'):[And(Regex('\w+'),len)],
                     Optional('abv'):And(float,lambda n:0 <= n <=100),
                     Optional('abw'):And(float,lambda n:0 <= n <=100),
                     Optional('ibu'):float,
                     Optional('reviews'):
                         [{'date': Regex('^\d{4}-\d{2}-\d{2}'),
                           Optional('group'):And(Regex('\w+'),len),
                           Optional('place'):And(Regex('\w+'),len),
                           Optional('count'):int, 
                           Optional('review_type'):And(float,lambda n:0 <= n <=10), 
                           Optional('review_over'):And(float,lambda n:0 <= n <=10),
                           Optional('review_uniq'):And(float,lambda n:0 <= n <=10),
                           Optional('comments'):[Regex('\w+')]}]}

drink_schema=Schema(drink_json_schema)
