class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

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





def count_n_children(t,n):
    if len(t.branches) == n:
        return 1 + sum([count_n_children(b,n) for b in t.branches])
    return sum([count_n_children(b, n) for b in t.branches])
        
def prune(t):
    def prune_level(t, d):
        if d % 2 == 0:
            t.branches = [b for b in t.branches if b.label >= t.label]
        else:
            t.branches = [b for b in t.branches if b.label <= t.label]
        for b in t.branches:
            prune_level(b, d + 1)

    prune_level(t, 0)

#tree review
def contains_word(w1, w2):
    """
    >>>contains_word("abefdacsy", "easy"):
    True
    >>>contains_word("abcdefg", "easy"):
    False
    """
    #no helper func
    #自己的
    """
    if not w1 and w2:
        return False
    elif not w1 and not w2:
        return True
    elif w1[0] == w2[0]:
        return contains_word(w1[1:], w2[1:])
    else:
        return contains_word(w1[1:], w2)
        """
    
    #老师的
    if len(w2) == 0: #这个顺序很重要，如果两个list都刚好是最后一个时候，这个在前面才会return True
        return True
    if len(w1) == 0:
        return False
    with_word = w1[0] == w2[0] and contains_word(w1[1:], w2[1:])
    without = contains_word(w1[1:], w2)
    return with_word or without

#dog 走min路线吃max东西， 具体看ipad
def trail_of_treats(G):
    return trail_helper(G, 0,0)

def trail_helper(G, x, y):
    if x == len(G) - 1 and y == len(G) - 1:
        return G[x][y]
    elif x > len(G) - 1 or y > len(G) - 1:
        return -1
    else:
        up = trail_helper(G, x, y + 1)
        right = trail_helper(G, x + 1, y)
        return max(up, right) + G[x][y]


#knapsack: 找出最好的comnination (这题答案不对)
def knapsack(capacity, weights, values):
    """
    >>>knapsack(5, [1, 5, 4], [3, 4, 5])
    8
    """

    if capacity <= 0 or len(weights) == 0:
        return 0
    with_first = values[0] + knapsack(capacity - weights[0], weights[1:], values[1:])
    without_first = knapsack(capacity, weights[1:], values[1:])
    return max(with_first, without_first)

            
#yield from
def integers(n):
    yield n
    yield from integers(n + 1)
def intergers_c(n): #do the exactly same thing in a complex way 
    yield n
    for elem in integers(n+1): #这个记一下 考试出现过
        yield elem

y = [10, 14, 6]
def strangegen(x):
    yield y.pop()
    while True:
        yield y[x]
        x += 1
        y.append(x)
"""z = [strangegen(i) for i in range(3)]
next(z[0])
next(z[0])
next(z[2])
for gen in z:
    print(next(gen))"""

#print all elem in the lini list
def link_iterator(link):
    """
    >>>link = Link(1, Link(2, Link(3)))
    >>>for el in link_iterator(link):
        print (el)
    1 
    2
    3
    """
    while link is not Link.empty:
        yield link.first
        link = link.rest

def link_iterator_if(link):
    if link is not Link.empty:
        yield link.first
        yield from link_iterator_if(link.rest)

def amplify(f,x): #spring 15 final
    """
    >>>list(amplify(lambda x: x//2-1, 14))
    [14, 6, 2]
    >>>list(amplify(lambda s: s[1:], 'boxes'))
    ['boxes', ....]
    """
    while x:
        yield x
        x = f(x)


#link list
def link_do_dict(L): #spring19 mt2 4a
    """
    >>>L = Link(1, Link(2, Link(3, Link(4, Link(1, Link(5))))))
    >>>print(L)
    <1, 2, 3, 4, 5> #1, 3, 5 is the key
    >>>link_do_dict(L)
    {1: [2, 5], 3:[4]}
    >>>print(L)
    <1, 3, 1>
    """
    D = {}
    while L is not Link.empty and L.rest is not Link.empty:
        key, value = L.first, L.rest.first
        if key not in D:
            D[key] = [value]   #记住这个！！！！怎么添加！！！
        else:
            D[key].append(value)
        L.rest, L = L.rest.rest, L.rest.rest   
    return D

def both(a, b): #fa17 mt2 4a
    if b is Link.empty or a is Link.empty:
        return False
    if a.first > b.first:
        a, b = b, a
    return both(a.rest, b) or a.first == b.first



#tree
def pile(t):   #fall17 mt2 5a
    p = {}
    def gather(u, parent):
        if is_leaf(u):
            p[label(u)] = parent
        for b in branches(u):
            gather(b, (label(u), parent))
    gather(t, ())
    return p

def add_word(trie, word):  #sp19 mt2 6a
    if not word:
        return 
    branch = None
    for b in trie.branches:
        if word[0] == b.label:
            branch = b
    if not b.branch:
        branch = Tree(word[0])
        trie.branches.append(branch)
    add_word(branch, word[1:])




