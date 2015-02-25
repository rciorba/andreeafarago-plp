import json
import glob


def min_max_average(array):
  minim=array[0]
  maxim=array[0]
  average=0.0
  for elem in array:
    if elem>maxim:
      maxim=elem
    if elem<minim:
      minim=elem
    average+=elem
  return "min " + str(minim) + ", max " + str(maxim) + ", average " + str(average/len(array))

all_files = glob.glob("scores/*.json")

for jsonfile in all_files:
  science = []
  math = []
  literature = []

  try:
    with open(jsonfile) as json_data:
      jsonobj = json.load(json_data)
  except IOError:
    print "The path is not valid"

  for obj in jsonobj:
    science.append(obj['science'])
    math.append(obj['math'])
    literature.append(obj['literature'])

  print jsonfile
  print '  science: ' + min_max_average(science)
  print '  math: ' + min_max_average(math)
  print '  literature: ' + min_max_average(literature)