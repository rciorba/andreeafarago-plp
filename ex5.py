#from string import digits
words_list = []
word_dictionary = {}

def get_dictionary(word_list):
  for word in word_list:
    # don't look in a dictionary's keys, it's slow
    # it takes the dict, extracts a list of keys
    # and does a sequential scan
    # use "key in dict" insted, it's much faster
    # using timeit we can see the difference,
    # from micro seconds to nano seconds
    # abouts 100 times slower
    # In [6]: %timeit "spam" in d.keys()
    # 100000 loops, best of 3: 2.12 µs per loop
    # In [7]: %timeit "spam" in d
    # 10000000 loops, best of 3: 37.4 ns per loop

    # if word in word_dictionary.keys():
    if word in word_dictionary:
      word_dictionary[word]=word_dictionary[word]+1
    else:
      word_dictionary[word] = 1
  return word_dictionary


def get_max(pairs):
  max_key, maxim = paris[0]
  for key, elem in pairs:
    if elem>maxim:
      maxim=elem
      max_key=key
  return max_key, maxim


try:
  file = open("filetostrip2.txt")
  # file = open("filetostrip.txt")
except IOError:
  print "The path is not valid. Try again..."

for line in file.read().splitlines():
  for word in line.split(' '):
    #print word.lower().translate(None, digits)
    stripped_list = ''.join(i for i in word.lower() if i.isalpha())
    words_list.append(stripped_list)


print words_list
print get_dictionary(words_list)
# for key, value in word_dictionary.items():
#     # get_max gets called an awful lot
#     if value == get_max(word_dictionary.values()):
#         print 'The word with the most occurrences is ' + str(key) + '. It has ' + str(value) + ' occurances.'

max_ = get_max(word_dictionary.iteritems())
for key, value in word_dictionary.items():
    # get_max gets called an awful lot
    if value == max_:
        print 'The word with the most occurrences is ' + str(key) + '. It has ' + str(value) + ' occ




