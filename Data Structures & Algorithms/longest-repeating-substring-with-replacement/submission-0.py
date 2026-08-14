class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap = {}
        currWindowSize = 0
        longestSubstring = 0
        l = 0

        for r in range(len(s)):
            countMap[s[r]] = countMap.get(s[r], 0) + 1
            currWindowSize += 1
            while currWindowSize -  max(countMap.values()) > k:
                currWindowSize-=1
                countMap[s[l]] -= 1
                l += 1
            longestSubstring = max(longestSubstring, r - l + 1)
        return longestSubstring

            
