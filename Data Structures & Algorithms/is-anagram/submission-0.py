class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        counts = {}
        counts2 = {}
        for char in s:
            counts[char] = counts.get(char, 0)+1
        for char in t:
            counts2[char] = counts2.get(char, 0)+1

        return counts == counts2
