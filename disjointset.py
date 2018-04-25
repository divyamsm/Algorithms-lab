class SetNode:
    def __init__(self,id = None):
        self.id = id
        self.parent = None
        self.rank = 0

def makeset(id,DSL):
    x  = SetNode(id)
    x.parent = x
    DSL.addset(x)
    return x

def findset(x):
    t = x
    if t.parent != t:                   #while t.parent ! = t:
        t.parent = findset(t.parent)            # t = t.parent
    return t.parent                        # return t

def union(x,y,DSL):
    t1 = findset(y)
    t2 = findset(x)
    if t1.rank > t2.rank:
        t2.parent = t1
        t1.id += t2.id
        DSL.delete(t2)
    elif t2.rank > t1.rank:
        t1.parent = t2
        t2.id += t1.id
        DSL.delete(t1)
    else :
        t1.parent = t2
        t2.id += t1.id
        t2.rank +=1
        DSL.delete(t1)

class DisjointSetList:
    def __init__(self):
        self.setlist = []

    def delete(self,x):
        self.setlist.remove(x)

    def addset(self,x):
        self.setlist.append(x)

    def printsets(self):
        for i in self.setlist:
            print(i.id)

DSL = DisjointSetList()
a = makeset('a',DSL)
b = makeset('b',DSL)
c = makeset('c',DSL)
d = makeset('d',DSL)
e = makeset('e',DSL)
union(c,d,DSL)
union(c,b,DSL)
DSL.printsets()
