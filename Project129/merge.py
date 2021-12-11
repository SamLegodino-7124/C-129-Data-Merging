import csv

data_set1 = []
data_set2 = []

with open("final.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data_set1.append(i)

with open("planet_data_sorted.csv", "r") as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        data_set2.append(i)

header1 = data_set1[0]
planet_data1 = data_set1[1:]

header2 = data_set2[0]
planet_data2 = data_set2[1:]

headers = header1 + header2

planet_data = []

for i,data in enumerate(planet_data1):
    planet_data.append(planet_data1[i]+planet_data2[i])

with open("merged_planet_data.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)