def leader_element(arr):
    n=len(arr)
    l=arr[n-1]
    arr1=[]
    for i in range(n-1,-1,-1):
        if arr[i]>=l:
            arr1.append(arr[i])
            l=arr[i]
    return arr1
arr=[16,17,4,3,5,2]
res=leader_element(arr)
print(res)


