class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for item in strs:
            count = [0] * 26
            for char in item:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            groups[key] = groups.get(key, []) + [item]
        return list(groups.values())
