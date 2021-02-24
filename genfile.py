'''
Generates files with names from 'input.txt' and 
fills it with random giberish data ... aka latin.
'''
import os
import shutil
import sys

DATA = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam nec efficitur erat, quis pulvinar purus. Suspendisse potenti. Fusce justo eros, vehicula sit amet felis in, congue semper dui. Phasellus porttitor dapibus diam non commodo. Phasellus massa sem, venenatis nec luctus eget, tristique ut ligula. Morbi convallis nisl at nulla pulvinar sollicitudin. Suspendisse eget rhoncus lectus. Sed venenatis erat arcu, id lacinia turpis mollis sit amet. Nulla luctus nibh augue, at feugiat leo cursus vel. Etiam sollicitudin eu eros ut interdum. 
'''.strip()

INPUT = './input.txt'

OUTPUT_ROOT = '/out'

if not os.path.exists(INPUT):
  print("Input path '{}' does not exist. Now exitting.".format(INPUT))
  sys.exit(-1)

if os.path.exists(OUTPUT_ROOT):
  print("There are files under '{}'. Deleting contents of '{}' before continuing.".format(OUTPUT_ROOT, OUTPUT_ROOT))
  for filename in os.listdir(OUTPUT_ROOT):
    os.remove(os.path.join(OUTPUT_ROOT, filename))
else:
  os.makedirs(OUTPUT_ROOT)

with open(INPUT) as f:
  
  filenames = [filename.strip() for filename in f.readlines()]
  for filename in filenames:
    
    full_filepath = os.path.join(OUTPUT_ROOT, filename) 
    with open(full_filepath, 'w') as output:
      
      print("Writing data to: {}".format(full_filepath))
      output.write(DATA)


