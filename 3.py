class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums)<=1:return nums
        else:
            pivot=nums[0]
            left=[i for i in nums[1:] if i<pivot]
            equal=[i for i in nums if i==pivot]
            right=[i for i in nums[1:] if i>pivot]
            return self.sortArray(left)+equal+self.sortArray(right)
sol=Solution()
print(sol.sortArray([5,2,3,1]))