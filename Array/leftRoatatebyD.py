# Left rotate the array by D place
class Solution:
    def reverse(self,nums,start,end):
        while start < end :
            nums[start],nums[end] = nums[end],nums[start]
            start+=1
            end-=1

    def rotateArray(self,nums,direction,k):
        n = len(nums)

        if n == 0 or k == 0:
             return nums

        k = k % n

        if direction == "left":
            #reverse first k element
            self.reverse(nums,0,k-1)

            #reverse remaining element
            self.reverse(nums,k,n-1)

             #reverse entire array
            self.reverse(nums,0,n-1)

        elif direction == "right":
            self.reverse(nums,0,n-1)

            self.reverse(nums,0,k-1)

            self.reverse(nums,k,n-1)

        return nums

nums=[1,2,3,4,5,6,7]
direction = "right"
k=2
Sol=Solution()

lt=Sol.rotateArray(nums,direction,k)
print(lt)



