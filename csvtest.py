import csv

passdictionary = {}

try:
  file = open("/etc/passwd")
except IOError:
  print "The path is not valid"

for line in file:
  if line.startswith("#"):
    pass
  else:
    splitline=line.split(":")
    key = splitline[0]
    value = splitline[2]
    passdictionary[key]=value

with open('csvfile.csv', 'w') as f:
  o = csv.writer(f, delimiter='\t')
  for i in passdictionary.keys():
    o.writerow([i, passdictionary[i]])