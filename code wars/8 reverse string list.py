def solution(string):

    stringb = []

    if len(string) == 0:
        stringb = ''.join(stringb)
        return stringb
    
    else:
        the_word = len(string)
        for i in range(the_word):
            backwards = i * -1
            stringb.append(string[backwards])

        a = stringb.pop(0)
        stringb.insert(len(stringb),a)
        print( stringb)
        stringb = ''.join(stringb)
        return stringb
        

def solution2(string):
    stringb = []
    for i in range(len(string)):
        backwards = i * -1
        stringb.append(string[backwards])
    print( stringb)
    stringb.insert(len(stringb),stringb.pop(0))
    stringb = ''.join(stringb)
    return stringb

