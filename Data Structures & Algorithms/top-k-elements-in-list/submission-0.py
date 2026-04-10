class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = []
        visited = []
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            visited.append(nums[i])
            c = 0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    c +=1
            count.append([c, nums[i]])
        count.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(count[i][1])
        return res