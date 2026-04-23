class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Brute-force method. TC: sorted(s)- O(nlogn) TC: sorted(t)- O(mlogm) SC- O(n+m)
        # sorted_s = ''.join(sorted(s))
        # sorted_t = ''.join(sorted(t))

        # if sorted_s == sorted_t:
        #     return True
        # else:
        #     return False

        # Using hashmap TC-O(n+m) SC - O(k) k = keys in count
        if len(s) != len(t):
            return False

        count = {}
        
        for c in s:
            count[c] = 1 + count.get(c,0)

        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -=1

        return True
        

        





        