## read from csv
# csv.reader() -> csv module

import csv  # -> have to import first

## have to create a seperate file name.csv eg employers.csv to read from with the data
# data is going to come in a certain format cannot always control

# next pull data from file that was created or the file you want to read data from

# rows = []
# #use open('file name',
# with open('employers.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile) # -> turns to reader file
#     header = next(csvreader) # -> column headers not
#     for row in csvreader: # -> looping through data
#         rows.append(row)
#
# print(f"The headers are: {header}")
# print(rows)

## write to csv
# csv.writer()

# # first create headers
# header = ['Name', 'Age']
# # then create data
# data = [['Joshna', 23], ['Jane', 24], ['Joey', 50]]
# #then use open function
# with open('student_info.csv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile) # -> created csv writer object
#     csvwriter.writerow(header) # -> creating row for headers
#     csvwriter.writerows(data) # -> rows for data
# # then create a new file with name you said in open function
# # if running and getting error says not writable with just open('student_info.csv') as csvfile just add 'w'

# challenge
# students = []
# with open('student_info.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)
#     for student in csvreader:
#         students.append(student)
#
# print(f"The students are: {header}")
# print(students)
#
# ## csv.dict reader
# # mapping and representing in a different way
# # another way of reading files into a dictionary format
#
# rows_2 = []
# with open ('employers.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row["Name"], row["email"])
#         print(row)

# write to csv file using dictwriter
# allows us to create an object
# dictionaries into csv data

# header = ['Name', 'Age']
# data = [['Joshna', 23], ['Jane', 24], ['Joey', 50]]
# # -> adding newline='' just gets rid of the gaps between data
# with open('student_info.csv', 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=header)
#     writer.writeheader()
#     for student in data:
#         writer.writerow({'Name': student[0], 'Age': student[1]})
#
# # namedtuple() - when importing a file, we can cast the incoming data to the namedtuple() for easier reading
#
# # -> adding 'r' opens as just readonly
#
# from collections import namedtuple
#
# with open('employers.csv', 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     Employee = namedtuple("Employee", next(reader), rename=True)
#     for row in reader:
#         employee = Employee(*row)
#         print(employee.Name, employee.Position, employee.email)

rows = []
#use open('file name',
with open('australia.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile) # -> turns to reader file
    header = next(csvreader) # -> column headers not
    for row in csvreader: # -> looping through data
        rows.append(row)

# print(f"The headers are: {header}")
# print(rows)
header.append('Capital')
data = [['Melbourne'], ['Sydney'], ['Adelaide'], ['Perth'],['Hobart'],['Brisbane'],['Canberra'],['Darwin']]

for index in range(len(rows)):
    rows[index].append(data[index][0])

with open('australia.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(rows)





