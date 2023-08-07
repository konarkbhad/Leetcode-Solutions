class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # time linear
        # space constant
        # Boyer Moore Algorithm
        maj, count = 0, 0
        
        for n in nums:
            if count == 0:
                maj = n
                
            if n == maj:
                count += 1
            else:
                count -= 1
        
        return maj
        
        # time linear
        # space linear
        count = {}
        maj, maxCount = 0, 0
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
            if count[n] > maxCount:
                maj, maxCount = n, count[n]
        
        return maj
    
    
        # time nlog(n)
        # space constant
        nums.sort()
        n = len(nums)
        return nums[n // 2]
        