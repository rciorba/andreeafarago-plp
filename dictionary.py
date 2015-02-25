#import collections

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

for i in sorted(passdictionary.keys()):
   print i +" = "+ passdictionary[i]


#od = collections.OrderedDict(sorted(passdictionary.items()))
#for k, v in od.iteritems(): print k, v