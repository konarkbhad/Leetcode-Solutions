class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        approach1:
left pointer -> to keep on val
right pointer -> not on val
when we are sure that right is not pointing to val, we keep this right ptr value on left.

        L L L
        3,0,3,0 val = 2
        R R R R R
        '''
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
        
        
        '''
#approach2:
#keeping all the vals on the end of the array.
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left
        '''