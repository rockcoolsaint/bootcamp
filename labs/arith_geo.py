def arith_geo(l):
    f = len(l)
    if f == 0:
        return 0
    elif f <= 2:
      return 0
    else:
        a = l[1] - l[0]
        b = l[2] - l[1]
        #e = l[3] - l[2]
        #f = l[4] - l[3]
        
        c = l[1]/l[0]
        d = l[2]/l[1]
        #x = l[3]/l[2]
        #y = l[4]/l[3]
        if (l[1] - l[0] == l[2] - l[1]) and (l[3]- l[2] == l[2] - l[1]):
          return 'Arithmetic'
        elif (l[1] / l[0] == l[2] / l[1]) and (l[3] / l[2] == l[2] / l[1]):
          return 'Geometric'
        else:
          return -1