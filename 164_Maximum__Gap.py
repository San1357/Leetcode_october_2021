# Err : Output Limit Exceeded.

# Note : 37 / 40 test cases passed.

# problem no: 164
# problem : Maximum Gap

# Approach 2 : by Radix sort 
            #  (sort the array using radix sorting, then iterate the sorted array & then find the max difference of successive elements)
            
# time : O(n)



class Solution:
    def counting(self,array, place):
        size = len(array)
        output = [0] * size
        count = [0] * 10

        # Calculate count of elements
        for i in range(0, size):
            index = array[i] // place
            count[index % 10] += 1

        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Place the elements in sorted order
        i = size - 1
        while i >= 0:
            index = array[i] // place
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, size):
            array[i] = output[i]
        print(array)
            

    # Main function to implement radix sort
    def maximumGap(self, array: List[int]) -> int:
        # Get maximum element
        max_element = max(array)

        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_element // place > 0:
            self.counting(array, place)
            place *= 10
            
        diff   = 0
        for i in range(len(array)-1):
            if array[i+1] - array[i] > diff:
                diff = array[i+1] - array[i]
        return diff
                
