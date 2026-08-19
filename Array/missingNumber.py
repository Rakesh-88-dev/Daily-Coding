def missingNumber(arr,n):
    n= len(arr)+1
    total_sum=sum(arr)
    expected_sum=n*(n+1)//2
    miss_num=expected_sum-total_sum
    return miss_num
    
    
arr=[1,2,3,5]
print(missingNumber(arr,5))    