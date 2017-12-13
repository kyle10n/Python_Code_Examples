from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['a'] = 'python'
favorite_languages['b'] = 'c+'
favorite_languages['c'] = 'C++'
favorite_languages['d'] = 'ruby'


for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

    
