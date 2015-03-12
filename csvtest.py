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

  # hmm.. using keys and looking the key up in the dict afterwords?
  for i in passdictionary.keys():
    o.writerow([i, passdictionary[i]])

  # a more elegant way to write the same thing:
  # for user_name, user_id in passdictionary.iteritems():
  #   o.writerow([user_name, user_id])

  # or even:
  # o.writerows(d.iteritems())

  # writers can accept a list of rows, and iteritems will happily
  # give you a list-like object
