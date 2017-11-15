### Day 04: have them put all the info they collected into a 
###		google spreadsheet 
###		To avoid using library to open csv, teacher should download
###		and turn into a .txt file, then slack to students as such

### Should discuss read vs readline, split by comma
### If possible, should also try out indexing and casting here


DataFile = open("Mineral data.txt")
DataFile.readline()
#DataString = DataFile.read()
#print(DataString)

# once you've done the read(), try readline() instead

Line1 = DataFile.readline().split(',')
print(Line1)

print(Line1[0])
print(type(Line1[0]))
print(float(Line1[0]))
print(int(Line1[0]))

