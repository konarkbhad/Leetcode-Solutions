class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time linear
        # space linear
        count = {}
        maj, maxCount = 0, 0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxCount:
                maj, maxCount = n, count[n]
        
        return maj
        