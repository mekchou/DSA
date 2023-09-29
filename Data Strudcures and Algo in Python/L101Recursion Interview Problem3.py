# Implement a Fibonnaci Sequence in three different ways:

# Recursively
# Dynamically (Using Memoization to store results)
# Iteratively
# Function Output
# Your function will accept a number n and return the nth number of the fibonacci sequence ___ Remember that a fibonacci sequence: 0,1,1,2,3,5,8,13,21,... starts off with a base case checking to see if n = 0 or 1, then it returns 1.

# Else it returns fib(n-1)+fib(n+2).


# Recursively

def fib_rec(n):
  if n == 1 or n == 0:
    return n
  else:
    return fib_rec(n-1) + fib_rec(n-2)
  pass
# print(fib_rec(10))


# Iteratively

def fib_iter(n):

  count = 1
  result = 0
  last1 = 1
  last2 = 0
  if n == 1 or n == 0:
    return n
  else:
    while count < n:
      result = last1 + last2
      last2 = last1
      last1 = result
      count += 1
    return result
# print(fib_iter(10))

    
  


  # pass

def fib_iter2(n):
    
    # Set starting point
    a = 0
    b = 1
    
    # Follow algorithm
    for i in range(n-1):
        # these operation run at the same time. in first iteration, a = 1, b = 0 + 1 = 1
        a, b = b, a + b
        # print(a)
        # print(a+b)
        # print(b)
    return b
# print(fib_iter2(2))
"""
UNCOMMENT THE CODE AT THE BOTTOM OF THIS CELL TO SELECT WHICH SOLUTIONS TO TEST.
THEN RUN THE CELL.
"""

from nose.tools import assert_equal

class TestFib(object):
    
    def test(self,solution):
        assert_equal(solution(10),55)
        assert_equal(solution(1),1)
        assert_equal(solution(23),28657)
        print('Passed all tests.')
# UNCOMMENT FOR CORRESPONDING FUNCTION
t = TestFib()

t.test(fib_rec)
#t.test(fib_dyn) # Note, will need to reset cache size for each test!
t.test(fib_iter)
t.test(fib_iter2)