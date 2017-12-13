def get_sum(a,b):
    #good luck!
    sum = 0
    c = abs(a - b)
    if a == b:
        return a
    else:
        d = min(a,b)
        while d <= max(a,b):
            sum += d
            d += 1
        return sum
        
        
