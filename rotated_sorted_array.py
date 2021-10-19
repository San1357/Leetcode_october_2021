# Leetcode Problem: Search in Rotated Sorted Array

#Leetcode problem no: 33

class Solution(object):
    def search(self, nums, target):
        
        lo, hi = 0, len(nums)-1
        
        while lo<=hi:
            
            mid = lo + ((hi - lo)//2)
            print(mid)
            
            if nums[mid]==target:
                return mid
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1
                    
        return -1
