# -*- coding: utf-8 -*-


class CSV_Writer:

    def __init__(self,pub,lines):
        self.lines=lines
        self.drink_column_order=[{"name":"Ölets namn"},{"country":"Land"},{"brewery":"Bryggeri"}]
        self.review_column_order=[{"date":"Provdatum"},{"count":"Antal Provare"},{"review_over":"Medelbetyg"},{"review_type":"Medelbetyg för öltyp"},{"review_uniq":"Medelbetyg för unik/intressant"}]
        self.csv_drink_order=[a.keys()[0] for a in self.drink_column_order]
        self.csv_review_order=[a.keys()[0] for a in self.review_column_order]
        self.csv_drink_order_values=[a.values()[0] for a in self.drink_column_order]
        self.csv_review_order_values=[a.values()[0] for a in self.review_column_order]
        self.list_of_lines=[]
        colon_names_list=[]
        colon_names_list.extend(self.csv_drink_order_values)
        colon_names_list.extend(self.csv_review_order_values)
        colon_names=','.join(colon_names_list)
        self.list_of_lines.append(colon_names)
        self.pub=pub

    def value_str(self, in_value):
        if isinstance(in_value,list):in_value=in_value[0]
        if isinstance(in_value,int) or isinstance(in_value,float): return str(in_value)
        elif isinstance(in_value,unicode): return in_value.encode("utf-8")
        else: return in_value
        
    def write_lines(self,filename):
        for drink_line in self.lines:
            for review_line in drink_line["reviews"]:
                write_line=[]
                for dcol in self.csv_drink_order:
                    if dcol in drink_line:
                        write_line.append(self.value_str(drink_line[dcol]))
                    else:
                        write_line.append("")
                for rcol in self.csv_review_order:
                    if rcol in review_line:
                        write_line.append(self.value_str(review_line[rcol]))
                    else:
                        write_line.append("")
                self.list_of_lines.append(','.join(write_line))
        with open(self.pub+"/"+filename,"w+") as s:
            s.write('\n'.join(self.list_of_lines))

                                        
            
