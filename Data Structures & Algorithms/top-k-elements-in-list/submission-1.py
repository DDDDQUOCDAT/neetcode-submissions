class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        freqDict = {}
        ans = []
        for i in nums:
            numDict[i] = numDict.get(i, 0) + 1
        for key, value in numDict.items():
            freqDict.setdefault(value,[]).append(key)
        while len(ans) < k:
            top = max(freqDict)
            ans.extend(freqDict.pop(top))
        return ans