class Solution:
    def findUnion(self,arr1,arr2,m,n):

        Union=[]
        i,j=0,0

        while i<m and j<n:
            if arr1[i] < arr2[j]:

                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i+=1

            elif arr2[j] < arr1[i]:
                if not Union or  Union[-1] !=arr2[j]:
                    Union.append(arr2[j])
                j+=1

            elif arr1[i] == arr2[j]:
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i+=1
                j+=1
        while i<m:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i+=1

        while j<n:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])

            j+=1

        return Union

if __name__ == "__main__":
    arr1=[1,2,3,4,5,6,7,8,9,10]
    arr2=[2,3,4,5,6,7,11,21]
    m=len(arr1)
    n=len(arr2)
    sol=Solution()
    k=sol.findUnion(arr1,arr2,m,n)
    print("Union of arr1 and arr2 is:", *k)                              

