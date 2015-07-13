def bsearch(a,n):
    last = len(a)-1
    first = 0
    while first <= last:
        if a[first] == n:
            return m
        elif a[last] == n:
            return m
        else:
            m = (first + last)//2
            if a[m] == n:
                return m
            else:
                if a[m] > n:
                    last = m - 1
                else:
                    first = m + 1