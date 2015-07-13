def find_max_min(n):
  if min(n) == max(n):
    return [len(n)]
  return [min(n),max(n)]