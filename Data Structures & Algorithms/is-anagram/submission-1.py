class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dicS = dict()
        dicT = dict()
        for i in range(len(s)):
            dicS[s[i]] = dicS.get(s[i], 0) + 1
            dicT[t[i]] = dicT.get(t[i], 0) + 1
        return (dicS==dicT)


