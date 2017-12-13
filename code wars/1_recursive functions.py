def digital_root(n):
    # ...
    a = sum(map(int,str(n)))
    if a < 10:
        return a
    else:
        n = a
        return digital_root(n)
