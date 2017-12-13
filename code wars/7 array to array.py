def count_positives_sum_negatives(arr):
    #your code here
    countera = 0
    counterb = 0
    cool = []
    empty = []
    for i in range(len(arr)):
        if arr[i] > 0:
            countera += 1
        else:
            counterb = counterb + arr[i]
    cool.append(countera)
    cool.append(counterb)

    print(len(arr))

    print( countera)
    print( counterb)


    if len(arr) == 0:
        return empty
    elif len(cool) == 0:
        return empty
    else:
        return cool
