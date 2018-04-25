def rec(arr,n):
    if (arr[n+1]>arr[n] and arr[n]>arr[n-1]):
        n= n + n-1
        return rec(arr,n)
    else:
        while not (arr[n]> arr[n-1] and arr[n]>arr[n+1]):
            n = n-1
        return arr[n]

def peak(arr):
    s = len(arr)
    n1 = 1 + (1+8*s)**0.5
    n2 = 1 - (1+8*s)**0.5
    n = n1 if n1>n2 else n2
    n = n//2
    p = rec(arr,n)
    return p

def bin(arr,n):
    if arr[n]>arr[n+1] and arr[n]> arr[n-1]:
        return arr[n]
    elif arr[n]>arr[n+1]:
        n = n//2
        return bin(arr,n)
    elif arr [n]<arr[n+1]:
        n = n + n//2
        return bin(arr, n)

def main():
    arr= [2,5,11,13,19,24,25,10,1,0,-5]
    #p = peak(arr)
    p = bin(arr,len(arr)//2)
    print(" The peak element is ",p)

if __name__=="__main__":
    main()