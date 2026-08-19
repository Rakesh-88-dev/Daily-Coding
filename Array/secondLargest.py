class Solution:
    def secondLargest(self,arr):

        large = arr[0]
        slarge = -1
        for i in range(1,len(arr)):
            if arr[i] > large:
                slarge=large
                large = arr[i]
            elif arr[i]>slarge and arr[i]<large:
                slarge=arr[i]
        return slarge
arr=[1,2,3,4,5,5,6,7]
S=Solution()
Sl=S.secondLargest(arr)
print(Sl)                
