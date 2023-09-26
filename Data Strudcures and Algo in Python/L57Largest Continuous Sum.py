def large_cont_sum(arr): 
  
  if len(arr) == 0:
     return 0

  maxresult = min(arr)

  for start in range(len(arr)):
    for end in range(start+1,len(arr)+1):
      result = sum(arr[start:end])
      # print(start,end,result)
      maxresult = max(result,maxresult)
  return maxresult


# print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]))
# print(large_cont_sum([-1,1]))

# solution1
def large_cont_sum2(arr): 
    
    # Check to see if array is length 0
    if len(arr)==0: 
        return 0
    
    # Start the max and current sum at the first element
    max_sum=current_sum=arr[0] 
    
    # For every element in array
    for num in arr[1:]: 
        
        # Set current sum as the higher of the two
        # if num is higher, we ignore what happened eariler, which may be negative num, so we start fresh with num
        current_sum=max(current_sum+num, num)
        
        # Set max as the higher between the currentSum and the current max
        max_sum=max(current_sum, max_sum) 
        
    return max_sum 


from nose.tools import assert_equal

class LargeContTest(object):
    def test(self,sol):
        assert_equal(sol([1,2,-1,3,4,-1]),9)
        assert_equal(sol([1,2,-1,3,4,10,10,-10,-1]),29)
        assert_equal(sol([-1,1]),1)
        assert_equal(sol([-1,2,-1,1]),2)
        print('ALL TEST CASES PASSED')
        
#Run Test
t = LargeContTest()
t.test(large_cont_sum)
t.test(large_cont_sum2)