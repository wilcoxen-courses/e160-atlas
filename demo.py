#! /bin/python3
#  Spring 2020 (PJW)

import json

#  Suppose a file of households has information about the name,
#  street address, and housing type (own or rent) for each 
#  household. To keep things simple, suppose there are two records
#  and they look like this:

hh_data = [
    "Smith|1234 Elm|own\n",
    "Jones|567 Oak|rent\n"
    ]

#  Creating a dictionary of the households using the names as 
#  the dictionary's key and a dictionary for each household to 
#  record its attributes, creating a blank list of occupants
#  along the way:

directory = {}

for line in hh_data:
    line = line.strip()
    fields = line.split("|")
    name = fields[0]
    new_hh = {
        'address':fields[1],
        'type':fields[2]
        }
    new_hh['occupants'] = []
    directory[name] = new_hh

#  Suppose that a file of occupants has the following information
#  about each person: their last name, their first name, their 
#  gender, and their year of birth. Further, suppose the contents
#  of it look like this:

pers_data = [
   'Smith|Alice|F|1980\n',
   'Smith|Ben|M|1981\n',
   'Smith|Carol|F|2010\n',
   'Jones|Dan|M|1993\n'
   ]

#  Adding this data to the directory of information about the 
#  households:

for line in pers_data:
    line = line.strip()
    fields = line.split("|")
    last = fields[0]
    new_pers = {
        'first':fields[1],
        'gender':fields[2],
        'dob':int(fields[3])
        }
    directory[last]['occupants'].append(new_pers)

#  Converting the directory to a JSON string and 
#  writing it out to a file:

json_str = json.dumps(directory,indent=4)
fh = open('households.json','w')
fh.write(json_str)
fh.close()

