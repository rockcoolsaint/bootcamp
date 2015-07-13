def words(s):
    dict = {}
    stringlst = s.split()
    for i in stringlst:
        occur = stringlst.count(i)
        if i.isdigit():
          i = int(i)
        dict[i] = occur
    return dict
