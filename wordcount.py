lineno=0
charno=0
whordno=0
uniquewordno=0
word_dictionary = {}
words = []

path = raw_input("Write input file path: ")

try:
  file = open(path)
except IOError:
  print "The path is not valid. Try again..."

for line in file.read().splitlines():
  lineno+=1
  charno+=len(line)
  words = line.split(' ')
  whordno+=len(words)
  for word in words:
    if word in word_dictionary.keys():
      pass
    else:
      word_dictionary[word] = "*value*"

print "Number of lines is " + str(lineno)
print "Number of words is " + str(whordno)
print "Number of chars is " + str(charno)
print "Number of unique words is " + str(len(word_dictionary))
print word_dictionary
