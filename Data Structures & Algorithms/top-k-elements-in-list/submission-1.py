class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1

        counter = dict(sorted(counter.items(), key = lambda x:x[1], reverse = True))
        
        return list(counter.keys())[:k]