class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n**2) . O(n)
        # output = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if j!= i:
        #             prod *= nums[j]

        #     output.append(prod)

        # return output

        output = [1]*len(nums)
        pre = 1
        post = 1

        for i in range(len(nums)):
            output[i] = pre 
            pre *= nums[i]

        for i in range(len(nums)-1,-1,-1):
            output[i] *= post
            post *= nums[i]

        return output 


