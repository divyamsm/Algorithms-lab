class Graph:
    def __init__(self,no):
        self.adjf = [[] for i in range(no)]
        self.incoming = [0 for i in range(no)]
        self.no = no
        self.sources = []

    def addedge(self,a,b):
        self.adjf[a].append(b)
        self.incoming[b] += 1

    def printgraph(self):
        for i in range(self.no):
            print( str(i) + " -> "+ str(self.adjf[i]))

    def count_sems(self):
        for i in range(self.no):
            if self.incoming[i]==0:
                self.sources.append(i)
        sems = 0
        while self.sources!=[]:
            tempsources = []
            for i in self.sources:
                for j in self.adjf[i]:
                    self.incoming[j]-=1
                    if self.incoming[j]==0:
                        tempsources.append(j)
            self.sources = tempsources
            sems+=1
        print("No of sems :" + str(sems))

if __name__=='__main__':
    f = open("graph1.txt",'r')
    no = int(f.readline())
    ed = int(f.readline())
    g = Graph(no)
    for i in range(ed):
        x = f.readline().split()
        x = list(map(int,x))
        g.addedge(x[0],x[1])
    g.count_sems()





