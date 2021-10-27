# Counting_Sort Algo:

def counting_sort(nums):
  size = len(nums)         
  output = [0] * size         # [0,0,0,0,0,0,0]
  count = [0] * 10            # [0,0,0,0,0,0,0,0,0,0]
  
  for i in range(size):       # final output for this loop : => [0,1,1+1,1+1,1,0,0,0,1,0] => [0,1,2,2,1,0,0,0,1,0]
    count[nums[i]] += 1
    
  for i in range(1,10):       # final output for this loop2 : => [0,1,3,5,6,6,6,6,7,7]
    count[i] += count[i-1]
    
  i = size - 1      
  while i>= 0:
    output[count[nums[i]]-1] = nums[i]
    count[nums[i]] -= 1
    i -= 1
    
  for i in range(size):
    nums[i] = count[i]
  print(nums)
    
count_sort([4, 2, 2, 8, 3, 3, 1])       
 
