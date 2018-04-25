def SolveHanoi(n, s, i, t):
    if n>1:
        SolveHanoi(n-1,s,t,i)
        print("Move topmost disc from ",s,"to ",t)
        SolveHanoi(n-1,i,s,t)

if __name__=="__main__":
    print("Enter the number of discs for tower of hanoi problem:")
    n = int(input())
    s = 'source'
    i = 'intermediate'
    t = 'target'
    SolveHanoi(n+1,s,i,t)

