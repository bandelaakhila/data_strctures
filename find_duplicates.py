class solution:
    def findDuplicates(self,nums):
        n=len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False
        
nums=list(map(int,input().split(',')))
sol=solution()
t1=sol.findDuplicates(nums)
print(t1)
