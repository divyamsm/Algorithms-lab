import sys
def newmatrix(n):
    a = [[sys.maxsize for i in range(n) ] for j in range(n)]
    return a
class Graph:
    def __init__(self,n):
        self.matrix = newmatrix(n)
        for i in range(n):
            self.matrix[i][i] = 0
        self.no = n

    def editedge(self,i,j,w):
        self.matrix[i][j] = w

#
# def floyd(g):
#         arr = [newmatrix(g.no) for i in range(g.no)]
#         arr[0] = g.matrix
#         for k in range(1,g.no):
#             for i in range(g.no):
#                 for j in range(g.no):
#                     arr[k][i][j] = min(arr[k-1][i][j], arr[k-1][i][k] + arr[k-1][k][j])
#         return arr[g.no - 1]

def floyd(g):
    #pi = [["." for i in range(g.no) ] for j in range(g.no)]
    currarr = []
    prevarr = g.matrix
    for k in range(g.no):
        currarr = newmatrix(g.no)
        for i in range(g.no):
            for j in range(g.no):
                currarr[i][j] = min(prevarr[i][j], prevarr[i][k] + prevarr[k][j])
                # pi[i][j] = pi[i][j] + " " + str(min(prevarr[i][j], prevarr[i][k] + prevarr[k][j]))
                #if prevarr[i][j]<( prevarr[i][k] + prevarr[k][j]):
                    #pi[i][j] = pi[i][j] + str(k)
        prevarr = currarr

    return prevarr

def main():
    f = open("floydgraph.txt", 'r')
    no = int(f.readline())
    ed = int(f.readline())
    g = Graph(no)
    for i in range(ed):
        x = f.readline().split()
        g.editedge(int(x[0]),int(x[1]),int(x[2]))
    ans = floyd(g)
    #print(ans)
    for i in range(no):
        for j in range(no):
            if ans[i][j]>100000:
                ans[i][j] = '#'
            print(ans[i][j], end = '  ')
        print()

if __name__=="__main__":
    main()