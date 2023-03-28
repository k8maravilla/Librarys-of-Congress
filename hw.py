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
