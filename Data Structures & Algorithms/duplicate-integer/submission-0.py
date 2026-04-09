class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False     O(n**2), O(1)

        #return len(nums) != len(set(nums)) O(n), O(n)

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True

        return False