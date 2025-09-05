import csv
import math
from functools import reduce

rows = []
total = 0
with open('../studentgrades.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

header.append('average grade')

for row in rows:
    total += int(row[1])

# highest_grade = reduce(lambda x, y: x > y, rows[1])
# print(highest_grade)

avarage = math.floor(total / len(rows))

for row in rows:
    row.append(avarage)

with open('../studentgrades.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)
    print("Hello hesed")

