# Approach 1: comparison approach through traversing
# problem no: 164
# problem name: maximum Gap

# time complexity : O(nlogn)
# space : 0(1)

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        diff   = 0
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i+1] - sorted_nums[i] > diff:
                diff = sorted_nums[i+1] - sorted_nums[i]
        return diff
                
        
        
        
        # time complexity : 
        
        # Sorted()  -  nlogn
        # for loop ()   - n
        
        #  => O(nlogn) +n
        #   => O(nlogn)
        
        
            
