def engage(i,j,husband,wife):
    wife[i][0]=j
    husband[j]=i

def gs(n,mpreference,wpreference,mnames,wnames):
    free_men= 5
    husband,wife = [-1 for i in range(n)],[[-1,0] for i in range(n)]
    while(free_men!=0):
        i=0
        while wife[i][0]!=-1:
            i+=1
        j=mpreference[i][wife[i][1]]
        if husband[j]==-1:
            engage(i,j,husband,wife)
            free_men-=1
            wife[i][1]+=1
            continue
        else:
            m=wpreference[j].index(husband[j])
            mm=wpreference[j].index(i)
            if mm<m:
                wife[husband[j]][0]=-1
                engage(i,j,husband,wife)
            else:
                wife[i][1]+=1
    for x in range(n):
        print( mnames[x] , " married ", wnames[wife[x][0]])

def main():
    print("Enter n")
    n = int(input())
    mpreference = [
        [1,0,3,4,2],
        [3,1,0,2,4],
        [1,4,2,3,0],
        [0,3,2,1,4],
        [1,3,0,4,2]
    ]
    wpreference=[
        [4,0,1,3,2],
        [2,1,3,0,4],
        [1,2,3,4,0],
        [0,4,3,2,1],
        [3,1,4,2,0]
    ]
    file = open("input.txt")
    mnames = str(file.readline())
    mnames = mnames.split()
    wnames = str(file.readline())
    wnames = wnames.split()
    num = len(mnames)
    mpref,wpref=[[] for i in range(num)],[[] for i in range(num)]
    for i in range(num):
        r=str(file.readline()).split()
        r=r[1:]
        mpref[i] = [wnames.index(x) for x in r]
    for i in range(num):
        r = str(file.readline()).split()
        r = r[1:]
        wpref[i] = [mnames.index(x) for x in r]
    gs(n,mpref,wpref,mnames,wnames)


if __name__=="__main__":
    main()