class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        left ptr -> to keep the element that the right ptr 
        is pointing to
        
        right ptr -> will check with preceding if equal
        and when not equal means that is unique and will keep
        that on left ptr
        
        first element will always be unique
        so starting from 1 and not 0
        '''
        left = 1

        for right in range(1, len(nums)):
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        
        return left
    
    
    
    '''
        left = 0
        
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
        
        return left + 1
    '''
        