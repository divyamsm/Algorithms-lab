class Graph:
    def __init__(self, no):
        self.elist = []
        self.V = DisjointSetList(no)


class SetNode:
    def __init__(self, id=None):
        self.id = id
        self.parent = self
        self.rank = 0


class DisjointSetList:
    def __init__(self, n):
        self.no = n
        self.setlist = [self.makeset(i) for i in range(n)]

    def makeset(self, id):
        return SetNode(str(id))

    def findset(self, x):
        t = x
        if t.parent != t:
            t.parent = self.findset(t.parent)
        return t.parent

    def union(self, x, y):
        t1 = self.findset(y)
        t2 = self.findset(x)
        if t1.rank > t2.rank:
            t2.parent = t1
            t1.id += t2.id
            # self.delete(t2)
        elif t2.rank > t1.rank:
            t1.parent = t2
            t2.id += t1.id
            # self.delete(t1)
        else:
            t1.parent = t2
            t2.id += t1.id
            t2.rank += 1
            # self.delete(t1)

    def delete(self, x):
        self.setlist.remove(x)

    def printsets(self):
        for i in self.setlist:
            print(i.id)


def Kruskal(G):
    G.elist.sort(key=lambda x: x[2])
    for i in G.elist:
        x = G.V.findset(G.V.setlist[i[0]])
        y = G.V.findset(G.V.setlist[i[1]])
        if x == y:
            continue
        print(i[0], " - ", i[1])
        G.V.union(x, y)


# DSL = DisjointSetList()
# a = makeset('a',DSL)
# b = makeset('b',DSL)
# c = makeset('c',DSL)
# d = makeset('d',DSL)
# e = makeset('e',DSL)
# union(c,d,DSL)
# union(c,b,DSL)
# DSL.printsets()

if __name__ == '__main__':
    f = open("graph2.txt", 'r')
    no = int(f.readline())
    ed = int(f.readline())
    DSL = DisjointSetList(no)
    G = Graph(no)
    for i in range(ed):
        x = f.readline().split()
        x = list(map(int, x))
        G.elist.append((x[0], x[1], x[2]))
    Kruskal(G)
    G.V.printsets()
