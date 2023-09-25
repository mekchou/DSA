
# Find the Missing Element
# Problem
# Consider an array of non-negative integers. A second array is formed by shuffling the elements of the first array and deleting a random element. Given these two arrays, find which element is missing in the second array.

# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

# Input:

# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])

# Output:

# 5 is the missing number


def finder(arr1, arr2):
  # sort both array
  arr1.sort()
  arr2.sort()
  # check first element that's not match
  for num in range(len(arr2)):
    if arr1[num] != arr2[num]:
      return arr1[num]
    # else:
      # num += 1
  return arr1[-1]


  # print(arr1[num], "is the missing number")

# arr1 = [1,2,3,4,5,6,7]
# arr1 = [5,5,7,7]
# arr2 = [3,5,2,1,4,6]
# arr2 = [5,7,7]
# print(finder(arr1,arr2), "is the missing number")

# solution 1
def finder2(arr1,arr2):
    
    # Sort the arrays
    arr1.sort()
    arr2.sort()
    
    # Compare elements in the sorted arrays
    for num1, num2 in zip(arr1,arr2):
        if num1!= num2:
            return num1
    
    # Otherwise return last element
    return arr1[-1]

# solution2
import collections

def finder3(arr1, arr2): 
    
    # Using default dict to avoid key errors
    # it would generate key if it doesn't exist
    d=collections.defaultdict(int) 
    
    # Add a count for every instance in Array 1
    for num in arr2:
        d[num]+=1 
    
    # Check if num not in dictionary
    for num in arr1: 
        if d[num]==0: 
            return num 
        
        # Otherwise, subtract a count
        else: d[num]-=1 


# solution 3
def finder4(arr1, arr2): 
    result=0 
    
    # Perform an XOR between the numbers in the arrays
    for num in arr1+arr2: 
        result^=num 
        print(result)
        
    return result 



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestFinder(object):
    
    def test(self,sol):
        assert_equal(sol([5,5,7,7],[5,7,7]),5)
        assert_equal(sol([1,2,3,4,5,6,7],[3,7,2,1,4,6]),5)
        assert_equal(sol([9,8,7,6,5,4,3,2,1],[9,8,7,5,4,3,2,1]),6)
        print('ALL TEST CASES PASSED')

# Run test
t = TestFinder()
t.test(finder)
t.test(finder2)
t.test(finder3)
t.test(finder4)