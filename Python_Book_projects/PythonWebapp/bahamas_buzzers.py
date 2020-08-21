#method strip() removes "whitespace symbols" from line (\n,\t,\r)
#title() transforms string to "Header Style" (This Is The Header Style Example)


from datetime import datetime
import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v


pprint.pprint(flights)
print()


flights2 = {}
for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()
pprint.pprint(flights2)


#Creates copy of flights dictionary, with converted keys and values
fts = {convert2ampm(k): v.title() for k, v in flights.items()}


#Example of using nested generator inside other generator
#(list generator for flights times nested inside dictionary generator for destinations)
#creates dictionary where destination is a key and flight times list is assotiated value
when2 = {dest: [k for k,v in fts.items() if v==dest]
         for dest in set(fts.values())}
pprint.pprint(when2)


#example of using simple (list) generator (it creates list)
more_dests = [] #Not requiered actualy 
more_dests = [dest.title() for dest in flights.values()]

#example of using simple (dictionary) generator, Note: key and value should be binded (with ":" symbol)
more_flights = {convert2ampm(k): v.title() for k, v in flights.items()}


#example of using generator with 'if' filter (can be split in multiple lines)
just_freeport = {convert2ampm(k): v.title()
                 for k, v in flights.items()
                 if v == 'FREEPORT'}

