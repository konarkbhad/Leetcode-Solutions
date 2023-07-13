class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [2,11,15,7] target = 9
        key = diff
        value = index
        d = {7 : 0, -2 : 1, -6 : 2}
        '''
        prevMap = {} # difference : index
        
        for i in range(len(nums)):
            n = nums[i]
            if n in prevMap:
                return [prevMap[n], i]
            
            prevMap[target - n] = i
        