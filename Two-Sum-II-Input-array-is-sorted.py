# USING LINEAR SEARCH
# Problem : Two Sum II - Input array is sorted
# Problem no : 167
# Note : 18/19 test cases is only working  because it binary search problem but i solve through linear search  


#CODE:


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
                else:
                    j+=1
        else:
            return
                

