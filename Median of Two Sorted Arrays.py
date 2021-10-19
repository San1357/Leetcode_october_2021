#Leetcode Problem No: 4

#Problem : Median of Two Sorted Arrays

#Notes : time(O(1))

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums3 = sorted(nums1 + nums2)
        n = len(nums3)
        lo = 0
        hi = n - 1
        res = 0
        
        if n == []:
            return None
        
        if n % 2 == 0 :
            res = (nums3[((n//2)-1)] + nums3[(n//2)])/2
            return res
        else:
            midpoint = (lo + (hi - lo))//2
            return nums3[midpoint]
        
