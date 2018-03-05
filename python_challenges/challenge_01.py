weird_to_correct = {'a':'c',
                    'b':'d',
                    'c':'e',
                    'd':'f',
                    'e':'g',
                    'f':'h',
                    'g':'i',
                    'h':'j',
                    'i':'k',
                    'j':'l',
                    'k':'m',
                    'l':'n',
                    'm':'o',
                    'n':'p',
                    'o':'q',
                    'p':'r',
                    'q':'s',
                    'r':'t',
                    's':'u',
                    't':'v',
                    'u':'w',
                    'v':'x',
                    'w':'y',
                    'x':'z',
                    'y':'a',
                    'z':'b'}


def string_swapper(string):
    """take a string and then change each alphabet to two
    alphabets forward"""

    the_list = string.split()
    new_list = []
    for word in the_list:

