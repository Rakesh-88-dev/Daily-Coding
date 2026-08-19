# Left rotate the array by one place 

class Solution:
    def leftRotate(self,arr):
        temp = arr[0]
        for i in range (1,n):
            arr[i-1] = arr[i]
        arr[n-1]=temp

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    n=len(arr)
    S= Solution()
    Rt = S.leftRotate(arr)
    print(arr[:Rt])
