class Solution:
    def largestElement(self,arr):
        large=arr[0]
        for i in range(1,len(arr)):
            if arr[i]>large:
                large=arr[i]
        return large

if __name__=="__main__":
    arr=[1,2,3,4,5,6]
    S=Solution()
    l=S.largestElement(arr)
    print(l)