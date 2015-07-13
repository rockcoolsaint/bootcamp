def data_type(val):
  if type(val) == None:
    return 'no value'
  elif type(val) == str:
    return len(val)
  elif val == None:
    return "no value"
  elif type(val) == bool:
    return val
  elif type(val) == int:
    if val < 100:
      return "less than 100"
    elif val > 100:
      return "more than 100"
    else:
      return "equal to 100"
  elif type(val) == list:
    if len(val) >= 3:
      return val[2]
    else:
      return None