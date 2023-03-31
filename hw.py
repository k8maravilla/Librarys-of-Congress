#problem 1 answer
'''def find_key(dictionary, value):
  answer = [ke for ke, val in dictionary.items() if val == value ]
  return answer[0] '''

#problem 2 answer
'''def move_to_bottom(diction, key):
  tru_fal = diction.get(key)
  if tru_fal is not None:
    diction[key] = diction.pop(key)
    return diction
  else:
    return "The key is not in the dictionary"'''

#problem 3 answer
'''def swap(diction):
  try:
    my_items = diction.items()
    swtch = {value: key for key, value in my_items}
    return swtch
  except:
    return "Cannot swap the keys and values for this dictionary"'''

#problem 4 answer
'''values = (dict, list, set, tuple)

def is_nested(dictionary):
  my_values = list(dictionary.values())
  for i in my_values:
    type_value = type(i)
    if type_value == tuple or type_value == dict or type_value == list:
      return True 
  return(False)
'''

#problem 5 answer
import json
def compare(file1, file2):
  file1_length = 0
  file2_length = 0

  with open(file1, 'r') as file, open(file2, 'r') as f:
    my_dict1 = json.load(file)
    my_dict2 = json.load(f)
    file1_length = len(my_dict1)
    file2_length = len(my_dict2)


  if my_dict1 == my_dict2:
    return 'The dictionaries are equal'
  elif file1_length > file2_length:
    return 'Dictionary 1 is longer than dictionary 2'
  elif file1_length < file2_length:
    return 'Dictionary 2 is longer than dictionary 1'
  elif file1_length == file2_length:
    return 'Dictionary 1 and dictionary 2 have the same length'