file = open("Assigments programs APP/input.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

first_two = lines[:2]

file.close()

output = open("Assigments programs APP/output.txt", "w")

for line in first_two:
    output.write(line)

output.close()

print("First two lines are written to output.txt")