class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        maxFreq = 0
        l = 0
        freq = {}

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(freq[s[r]],maxFreq)

            while (r - l + 1) - maxFreq > k:
                freq[s[l]] -= 1  # remove the char at left end
                l +=1


            maxLen = max(maxLen, r - l + 1)

        return maxLen