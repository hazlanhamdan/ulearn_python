import json

s = u'{"coord":{"lon":101.69,"lat":3.14},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":304.8,"pressure":1007,"humidity":66,"temp_min":303.15,"temp_max":306.15},"visibility":10000,"wind":{"speed":3.1,"deg":230},"clouds":{"all":75},"dt":1439454263,"sys":{"type":1,"id":8138,"message":0.0131,"country":"MY","sunrise":1439421086,"sunset":1439465088},"id":1733046,"name":"Kuala Lumpur","cod":200}\n'

d = json.loads(s)

TAB = '    '

def print_number(n, level):
    print TAB * level, n

def print_string(s, level):
    print TAB * level, s

def print_list(s, level):
    print TAB*level, 'list ==>',
    for el in s:
        pretty_print(el, level)

def print_dict(d, level):
    for key, value in d.iteritems():
        print TAB * level, key, '==>',
        pretty_print(value, level)

def pretty_print(o, level=-1):
    if type(o) == dict:
        print_dict(o, level+1)
    elif type(o) == int or type(o) == float:
        print_number(o, level+1)
    elif type(o) == unicode or type(o) == str:
        print_string(o, level+1)
    elif type(o) == list:
        print_list(o, level+1)
    else:
        import sys
        print 'invalid type:', type(o)
        sys.exit()

pretty_print(d)
#pretty_print([1, 2, [3, [4, [5,]]]])
