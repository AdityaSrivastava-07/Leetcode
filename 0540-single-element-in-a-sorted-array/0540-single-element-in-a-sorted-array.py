class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=0
        e=len(nums)-1
        while s<e:
            m=s+(e-s)//2
            if m%2==1:
                m-=1
            if nums[m]==nums[m+1]:
                s=m+2
            else:
                e=m
        return nums[s]
