# Let's think about what the steps we need to take here are:

# Iterate through the initial string – e.g., ‘abc’.
# For each character in the initial string, set aside that character and get a list of all permutations of the string that’s left. So, for example, if the current iteration is on 'b', we’d want to find all the permutations of the string 'ac'.

# Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add to our final results.

# Return the list of final results.


def permute(s):
  output = []
  
  #base case
  if len(s) <= 1:
    output = [s]
  #recursion
  # for every letter in string
  else:
    for i, letter in enumerate(s):
      # for every permutation resulting from step 2 and 3
      for perm in permute(s[:i] + s[i+1:]):
        output += [letter + perm]
  return output



  pass

"""
RUN THIS CELL TO TEST YOUR SOLUTION.
"""

from nose.tools import assert_equal

class TestPerm(object):
    
    def test(self,solution):
        
        assert_equal(sorted(solution('abc')),sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba']))
        assert_equal(sorted(solution('dog')),sorted(['dog', 'dgo', 'odg', 'ogd', 'gdo', 'god']) )
        
        print('All test cases passed.')
        


# Run Tests
t = TestPerm()
t.test(permute)