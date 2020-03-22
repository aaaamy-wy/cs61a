from math import gcd
class Rational:
    def __init__(self, numerator, denominator):
        n = gcd(numerator, denominator)
        self.numerator = numerator //  n
        self.denominator = denominator // n
    def print(self):
        if self.denominator == 1:
            print(self.numerator)
        else:
            print(self.numerator, '/', self.denominator)


class Animal:
    legs = 0
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
   
class dog(Animal):
    legs = 4
    def speak(self):
        return 'woof!'
    def fetch(self, item):
        print('I fetch' + str(item))

class chicken(Animal):
    legs = 2
    def speak(self):
        return 'cluck!'

class goldenRetriever(dog):
    def speak(self):
        return dog.speak(self)

class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest 

def sum_link(lnk):
    if lnk is Link.empty:
        return 0
    return lnk.first + sum_link(lnk.rest)

def display_link(lnk):
    string = "< "
    while lnk is not Link.empty:
        if isinstance(lnk.first, Link):
            elem = display_link(lnk.first)
        else:
            elem = str(lnk.first)
        string += elem + " "
        lnk = lnk.rest
    return string + '>'

def map(f, lnk):
    """
    >>> lnk1 = Link(1, Link(2, Link(3)))
    >>> a = map(lambda x: x*2, lnk1)
    >>> display_link(a)
    '< 2 4 6 >'
    """
     
    if lnk is Link.empty:
        return Link.empty
    else:
        return Link(f(lnk.first), map(f,lnk.rest))

def map_iter(f, lnk):
    new_link = Link.empty
    while lnk is not Link.empty:
        new_link = Link(f(lnk.first), new_link)  #这样子出来是反过来的， link list 没有办法让它在后面添加
        lnk = lnk.rest
    return new_link

#mutation
#mutation 可以recursion 和 iteration
"""def map2(lnk, f):
    if lnk is Link.empty:
        return 
    lnk.first = f(lnk.first)
    map2(l nk.rest, f)"""


def map2_iter(lnk, f):
    while lnk is not Link.empty:
        lnk.first = f(lnk.first)
        lnk = lnk.rest


class A:
    def __repr__(self):
        return 'A'



    





   



