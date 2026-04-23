class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force. TC- O(n**2) SC- O(1)
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i,j]

        # return False

        # Using hashmap. O(n) .. O(n)
        num_to_index = {} # dictionary
        for i,num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement],i]
            num_to_index[num] = i

        return False
