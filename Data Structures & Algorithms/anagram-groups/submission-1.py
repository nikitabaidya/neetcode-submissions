class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        #Each position tracks whether the string 
        #at that index has already been assigned to an anagram group.
        used = [False] * len(strs)
        
        for i in range(len(strs)):
            if used[i]:
                continue
                
            # Start a new group with strs[i]
            current_group = [strs[i]]
            used[i] = True
            
            # Compare with all remaining strings
            for j in range(i + 1, len(strs)):
                if not used[j] and self.isAnagram(strs[i], strs[j]):
                    current_group.append(strs[j])
                    used[j] = True
            
            result.append(current_group)
        
        return result
    
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if two strings are anagrams
        if len(s) != len(t):
            return False
        
        # Count characters (assuming lowercase letters)
        # else convert to lower case
        s = s.lower()
        t = t.lower()
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        for char in t:
            count[ord(char) - ord('a')] -= 1
        
        return all(c == 0 for c in count) # True

        
