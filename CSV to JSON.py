import csv
import json

file = open("Assigments programs APP/input.csv", "r")

data = csv.DictReader(file)

records = list(data)

file.close()

output = open("Assigments programs APP/output.json", "w")

json.dump(records, output, indent=4)

output.close()

print("CSV data converted to JSON successfully.")