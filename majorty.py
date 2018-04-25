import math
def eq(a,b):
    return a==b

def majority_element(arr,start,end):
    if end == start :
        return arr[start]
    if end == start+1 :
        if eq(arr[start],arr[end]):
            return arr[start]
    else :
        a = majority_element(arr,start,(start+end)//2)
        c = 0
        for i in arr:
            if i == a:
                c+=1
        if c > len(arr)//2:
            return a
        b = majority_element(arr, ((start + end) // 2) + 1, end)
        c = 0
        for i in arr:
            if i == b:
                c+=1
        if c > len(arr)//2:
            return b


no = int(input("Enter the number of elements"))
arr = []
for i in range(no):
    arr.append(input())
print("Majority element :" + str(majority_element(arr,0,len(arr)-1)))

