#from string import digits
words_list = []
word_dictionary = {}

def get_dictionary(word_list):
  for word in word_list:
    if word in word_dictionary.keys():
      word_dictionary[word]=word_dictionary[word]+1
    else:
      word_dictionary[word] = 1
  return word_dictionary


def get_max(array):
  maxim=array[0]
  for elem in array:
    if elem>maxim:
      maxim=elem
  return maxim


try:
  file = open("filetostrip2.txt")
  # file = open("filetostrip.txt")
except IOError:
  print "The path is not valid. Try again..."

for line in file.read().splitlines():
  for word in line.split(' '):
    #print word.lower().translate(None, digits)
    stripped_list = ''.join(i for i in word.lower().strip() if i.isalpha())
    words_list.append(stripped_list)


print words_list
print get_dictionary(words_list)
for key, value in word_dictionary.items():
    if value == get_max(word_dictionary.values()):
        print 'The word with the most occurrences is ' + str(key) + '. It has ' + str(value) + ' occurances.'





