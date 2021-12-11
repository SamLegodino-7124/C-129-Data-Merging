import csv

data = []

with open("planet_data_table.csv", 'r') as f:
    csv_reader = csv.reader(f)

    for i in csv_reader:
        data.append(i)

headers = data[0]
planet_data = data[1:]

#converting all planet names into lower case
for i in planet_data:
    i[0] = i[0].lower()

#sorting planet names in alphabetical order
planet_data.sort(key = lambda planet_data:planet_data[0])

with open("planet_data_sorted.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
