#Move Zeros To End 
class Solution:
    def moveZeros(self,arr):
        j=-1
        for i in range(len(arr)):
            if arr[i]==0:
                j=i
                break
        
        if j==-1:
            return None
        
        for i in range(j+1,len(arr)):
            if arr[i] != 0:
                arr[i],arr[j] = arr[j],arr[i]
                j+=1

sol=Solution()
arr = [1,0,2,0,0,0,0,3,4,5,6]
result=sol.moveZeros(arr)
print(arr[:result])
