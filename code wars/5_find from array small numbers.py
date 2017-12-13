def sum_two_smallest_numbers(numbers):
    #your code here
    numbers2 = numbers
    a = min(numbers2)
    numbers2.remove(a)
    b = min(numbers2)
    return a+b
