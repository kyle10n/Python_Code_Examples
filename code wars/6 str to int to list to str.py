

def high_and_low(numbers):
    # ...
    x = [int(i) for i in numbers.split()]
    a = max(x)
    b = min(x)

    print('"',a," ", b,'"',sep = '')
