def main():
    arr= [4,10,8,2,1]
    cnt = 0
    i1,i2 = 0,0
    while i1!= len(arr)-1:
        if arr[i1]>arr[i2]:
            cnt+=1
        if i2 == len(arr)-1:
            i1+=1
            i2= i1
            continue
        i2+=1
    print(" The no. of inversion pairs is ",cnt)

if __name__=="__main__":
    main()