#Problem: Find Minimum in Rotated sorted array 
#Leetcode Problem : 153

#Code:
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) -1
        if len(nums) == []:
            return 
        if len(nums) == 1:
            return nums[0]
        while lo < hi :
            mid = lo + (hi - lo)//2
            if nums[mid] > nums[mid +1] and nums[mid] > nums[mid-1]:
                return nums[mid+1]
            if nums[mid] < nums[mid-1] and nums[mid] <nums[mid+1]:
                return nums[mid]
            
            elif nums[mid] < nums[lo] :
                hi = mid -1
            elif nums[mid] > nums[hi]:
                lo = mid+1
            else:
                return nums[0]
        
