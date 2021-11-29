# Tema1 lista de masini
import csv
import random
import json
import os

list_cars = []
with open('Cars.csv', 'r') as fisier_cars:  # read the cars from the csv file and add them to the list of dictionary
    rows = csv.reader(fisier_cars, delimiter=',')
    for row in rows:
        dict_of_row = {"id": '', "brand": row[0], "model": row[1], "hp": row[2], "price": row[3]}
        list_cars.append(dict_of_row)

list_ids = random.sample(range(12345, 98765), 9)  # creates a list with unique ids
# print("Unique ids: ",list_ids)

i = 0
for dict in list_cars:  # assign a unique id for each car from the list
    dict["id"] = list_ids[i]
    i = i + 1

# for item in list_cars:
#     print(item)

# clasify cars

slow_cars = list(filter(lambda car: int(car.get("hp")) < 120, list_cars))
fast_cars = list(filter(lambda car: 120 <= int(car.get("hp")) < 180, list_cars))
sport_cars = list(filter(lambda car: int(car.get("hp")) >= 180, list_cars))

cheap_cars = list(filter(lambda car: int(car.get("price")) < 1000, list_cars))
medium_cars = list(filter(lambda car: 1000 <= int(car.get("price")) < 5000, list_cars))
expensive_cars = list(filter(lambda car: int(car.get("price")) >= 5000, list_cars))
# for item in slow_cars:
#     print(item)

# write the json.files and delete the ones that are empty or non existent

with open('slow_cars.json', 'w') as outfile:
    json.dump(slow_cars, outfile)
if not slow_cars:
    os.remove('slow_cars.json')

with open('fast_cars.json', 'w') as outfile:
    json.dump(fast_cars, outfile)
if not fast_cars:
    os.remove('fast_cars.json')

with open('sport_cars.json', 'w') as outfile:
    json.dump(sport_cars, outfile)
if not sport_cars:
    os.remove('sport_cars.json')

with open('cheap_cars.json', 'w') as outfile:
    json.dump(cheap_cars, outfile)
if not cheap_cars:
    os.remove('cheap_cars.json')

with open('medium_cars.json', 'w') as outfile:
    json.dump(medium_cars, outfile)
if not medium_cars:
    os.remove('medium_cars.json')

with open('expensive_cars.json', 'w') as outfile:
    json.dump(expensive_cars, outfile)
if not expensive_cars:
    os.remove('expensive_cars.json')

# create a file for each brand
list_brands = [d['brand'] for d in list_cars if 'brand' in d]
list_brands = list(dict.fromkeys(list_brands)) # remove duplicate brands
print(list_brands)

for brand in list_brands:
    list_current_brand = [elem for elem in list_cars if elem["brand"] == brand]
    # print(list_current_brand)
    # print('--------')
    with open('brands/'+brand+'.json', 'w') as outfile:
        json.dump(list_current_brand, outfile)

files = os.listdir('/Users/carafaf/Documents/Curs Python/Pycharm programs/Tema_memory_savers/brands') # updates the files with car brands
files = [f.split('.')[0] for f in files]
# print(files)
for f in files:
    if f not in list_brands:
        os.remove('brands/' + f + '.json')