def reverse_string(strings):
  if strings:
    return reverse(strings)
    if strings == reverse(strings) :
      return True
  else:
    return None


def reverse(strings) :
  rev = ""
  for i in range(0, len(strings)):
    rev += strings[(len(strings) -1) -i]
  return rev