class Solution:
    def FindMaxConsecutiveOnes(self,nums):
        cnt=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                cnt=0
            maxi=max(maxi,cnt)
        return maxi

nums=[1,0,1,1,1,0,0,1,1,0]
obj=Solution()
ans=obj.FindMaxConsecutiveOnes(nums)
print(ans)                