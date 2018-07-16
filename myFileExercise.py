fileName = "arrayFile.txt"

nameArray = ["Jordan", "Caleb", "Kevin", "Maddie", "Miyah"]
my_file = open(fileName, "w+")

for item in nameArray:
    my_file.write(item + "\n")

