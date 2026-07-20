import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
list= []
try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            parts = row["name"].split(", ")
            lastname= parts[0]
            firstname= parts[1]
            student_dict= {"first": firstname, "last": lastname, "house": row["house"]}
            list.append(student_dict)
except FileNotFoundError:
    sys.exit("Could not read" + sys.argv[1])

with open(sys.argv[2], "w") as file:
    headers= ["first", "last", "house"]
    writer= csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    for student in list:
        writer.writerow(student)
