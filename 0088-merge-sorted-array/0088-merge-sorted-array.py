class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1 # last index in nums1
        m -= 1
        n -= 1
        
        # fill in reverse order
        while m >= 0 and n >= 0:
            if nums1[m] < nums2[n]:
                nums1[last] = nums2[n]
                n -= 1
            else:
                nums1[last] = nums1[m]
                m -= 1
            last -= 1
        
        # fill nums1 with leftovers from nums2
        # will have leftovers if nums2 have small elements than nums1 nums1 = [1, 0] nums2 = [0]
        while n >= 0:
            nums1[last] = nums2[n]
            last -= 1
            n -= 1
            
        

                
                