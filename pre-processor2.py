import pandas as pd
import csv

df = pd.read_csv('dwarf_stars.csv')
df = df[df['Star_name'].notna()]
df = df[df['Mass'].notna()]
df = df[df['Radius'].notna()]
df = df[df['Distance'].notna()]

# data = []
# with open('dwarf_stars.csv', 'r') as f:
#     csvreader = csv.reader(f)
#     for rows in data:
#         data.append(rows)

headers = ['row_num', 'star_name', 'distance', 'mass', 'radius']
planet_data = []
mass = df['Mass']
radius = df['Radius']
star_name = df['Star_name']
distance = df['Distance']

for pl_mass in mass:
    planet_mass = float(pl_mass)*0.000954588
    planet_data.append(planet_mass)

for pl_radius in radius:
    planet_radius = float(pl_radius)*0.102763
    planet_data.append(planet_radius)

for pl_name in star_name:
    planet_data.append(pl_name)

for dis in distance:
    planet_data.append(dis)

with open('brown_dwarf_stars.csv', 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)