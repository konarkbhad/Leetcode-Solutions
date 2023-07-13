class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # solution if there is constraint that we can't modify the input array like by sorting it
        res, dups = set(), set()
        seen = {}
        
        for i, v1 in enumerate(nums):
            if v1 in dups:
                continue
            
            dups.add(v1)
            
            for j, v2 in enumerate(nums[i + 1:]):
                c = -v1 - v2 # number/complement needed for triplet to sum to 0
                if c in seen and seen[c] == i:
                    res.add(tuple(sorted((v1, v2, c))))
                seen[v2] = i    
                
        return res
    
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # write twoSumII in seperate function to simplify; hashSet can also be used in this
        # time O(nlogn) + O(n^2)
        # space O(1) or O(N), depending if sorting takes space
        
        '''
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        '''
        
        res = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            n = nums[i]
            if n > 0: # If the current value is greater than zero, break from the loop. Remaining values cannot sum to zero.
                return res
            
            if i > 0 and n == nums[i - 1]: # If the current value is the same as the one before, skip it.
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                curSum = n + nums[l] + nums[r]
                
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < len(nums) and nums[l] == nums[l - 1]:
                        l += 1
                    
        return res
            
        