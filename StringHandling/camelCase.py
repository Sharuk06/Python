#Program to implement camel case

def camel(x):
    list = [y for y in x.split()]
    camellist = [z.title() for z in list]
    camel = ' '.join(camellist)
    print camel

string = raw_input()
camel(string)
