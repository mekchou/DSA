# Array Pair Sum
# Problem
# Given an integer array, output all the ** unique ** pairs that sum up to a specific value k.

# So the input:

# pair_sum([1,3,2,2],4)

# would return 2 pairs:

#  (1,3)
#  (2,2)

#  FOR TESTING PURPOSES CHANGE YOUR FUNCTION SO IT OUTPUTS THE NUMBER OF PAIRS

# brute force method
def pair_sum_bf(arr,k):
  if len(arr) < 2:
    return 
  count = 0
  for i in range(len(arr)):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == k:
        # print("(", arr[i], ",", arr[j], ")")
        count += 1
      j += 1
    i += 1
  # print(count)
  return(count)
# pair_sum_bf([1,3,2,2],4)
# pair_sum_bf([1,2,3,1],3)
# pair_sum_bf([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
# pair_sum_bf([1],2)
  


def pair_sum(arr,k):
  # create empty set
  seen = set()
  output = set()
  # for every number in array
  for num in arr:
    # set target difference
    target = k - num
    # add to set if target hasn't been seen
    if target not in seen:
      seen.add(num)
    else:
      output.add((min(num, target),max(num, target)))
  return(len(output))
  # print(output)
  # print('\n'.join(map(str,list(output))))
  # print(len(output))
# pair_sum([1,3,2,2],4)
# pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
# pair_sum([1],2)

from nose.tools import assert_equal

class TestPair(object):
    
    def test(self,sol):
        assert_equal(sol([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10),6)
        assert_equal(sol([1,2,3,1],3),1)
        assert_equal(sol([1,3,2,2],4),2)
        print('ALL TEST CASES PASSED')
        
#Run tests
t = TestPair()
# t.test(pair_sum_bf)
t.test(pair_sum)
    