"""class Tree:
  
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches


    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()


# remove if  == to n
def pruning(t,n):
    """
   # >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1), [Tree(1), Tree(0)]])])
"""
    
    t.branches = [b for b in t.branches if b.label != n]
    for b in t.branches:
        pruning(b,n)



class Link:
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest 

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link(' + self.__repr__() + ')'  #repr(self.first) 也可以写成 self.__repr__()
        else:
            return 'Link(' + repr(self.first) + ', ' + repr(self.rest) + ')' #repr(self.first) 这个就直接把第一个数弄出来

    def __str__(self):
        s = '<'
        while self.rest is not Link.empty:
            s = s + str(self.first) + ', '
            self = self.rest
        return s + str(self.first) + '>'
    
    def __eq__(self, other):
        if self.first != other.first:
            return False
        return self.rest == other.rest
    
    def __contains__(self, x):
        if self.first == x:
            return True
        return x in self.rest

    def __add__(self, other):
        """
        
"""

        if self.rest is Link.empty:
            if other.rest is Link.empty:
                return Link(self.first, Link(other.first))
            else:
                return Link(self.first, Link(other.first) + other.rest)
        else:
            return Link(self.first, self.rest + other)"""

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'




def split(s, pred):
    satisfy, not_satisfy = Link.empty, Link.empty
    while s is not Link.empty:
        rest = s.rest
        if pred(s.first):
            satisfy = Link(s.first, satisfy)
        else:
            not_satisfy = Link(s.first, not_satisfy)
        s = rest
    return satisfy, not_satisfy    




