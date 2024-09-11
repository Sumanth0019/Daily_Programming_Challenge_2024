
def remove_duplicates(arr):
    arr1=arr2=arr[0]
    while True:
        arr1=arr[arr1]
        arr2=arr[arr[arr2]]
        if arr1==arr2:
            break
    arr1=arr[0]
    while arr1!=arr2:
        arr1=arr[arr1]
        arr2=arr[arr2]
    return arr2
arr=[3,1,3,4,2]
print(remove_duplicates(arr))
