def find_missing_num(arr):
    n=len(arr)+1
    total=n*(n+1)//2
    final=sum(arr)
    last=total-final
    return last
print(find_missing_num([1,2,4,5]))
print(find_missing_num([2,3,4,5]))
print(find_missing_num([1,2,3,4]))
print(find_missing_num([1]))