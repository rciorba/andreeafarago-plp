lineno=0
charno=0
whordno=0
uniquewordno=0
word_dictionary = {}
words = []

path = raw_input("Write input file path: ")

try:
  file = open(path)
  # file is a builtin, you shoudn't use this as a variable name
except IOError:
  print "The path is not valid. Try again..."
  # to nitpick, this tells the user there's a problem but then continues execution
  # and spewes a traceback

# for line in file.read().splitlines():
# no need to read the whole thing in to memory
# and then split it, just iterate over the file like so:
for line in file:
  lineno+=1
  charno+=len(line)
  words = line.split(' ')
  whordno+=len(words)
  for word in words:
    # never ever do this:
    # if word in word_dictionary.keys():
    if word in word_dictionary:
      pass
    else:
      word_dictionary[word] = "*value*"

print "Number of lines is " + str(lineno)
print "Number of words is " + str(whordno)
print "Number of chars is " + str(charno)
print "Number of unique words is " + str(len(word_dictionary))
print word_dictionary
