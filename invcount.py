import time
from random import randint
from matplotlib import pyplot

def split_inversions(a,b):
    cnt = 0
    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]>b[j]:
            cnt = cnt+ len(a)-i
            j+=1
        else:
            i+=1
    return cnt


def counting_inversions(arr):
    l = len(arr)
    if l==1:
        return 0
    al = arr[:l//2]
    ar = arr[l//2:]
    il = counting_inversions(al)
    ir = counting_inversions(ar)
    al.sort()
    ar.sort()
    isp = split_inversions(al,ar)
    return( isp+il+ir)

def naive(arr):
    cnt =0
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[j]<arr[i]:
                cnt+=1
    print(cnt)

if __name__=="__main__":
    arr=[]
    for i in range(256):
        arr.append(randint(0,999))
    print(arr)
    #for i in range(6):
    #    arr.append(int(input()))
    start = time.clock()
    n = counting_inversions(arr)
    print(n)
    print(time.clock() - start)
    start = time.clock()
    naive(arr)
    print(time.clock() - start)
