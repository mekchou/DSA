# Balanced Parentheses Check
# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced. We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. Assume that the string doesn’t contain any other character than these, no spaces words or numbers. As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced but ‘([)]’ is not.

# You can assume the input string has no spaces.


# Design: 
# create a set of opening
# create a set of matching pairs
# create a list to store temp result

# check if length is even number if not then false
# check every char, if it's opening, add to opening
# if not, 
#   if stack is empty then False
#   lastopen = stack.pop
#   if (lastopen,next char) not in matches then false
# finally, check if stack is empty


def balance_check(s):
  opening = set('([{')
  matches = set([('(',')'),('[',']'),('{','}')])
  stack = []

  if len(s) % 2 == 1:
    return False
  
  for char in s:
    if char in opening:
      stack.append(char)

    else:
      if len(stack) == 0:
        return False
      
      lastopen = stack.pop()

      if (lastopen, char) not in matches:
        return False
  return len(stack) == 0

print(balance_check('[]'))
print(balance_check('[](){([[[]]])}'))
print(balance_check('()(){]}'))


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal

class TestBalanceCheck(object):
    
    def test(self,sol):
        assert_equal(sol('[](){([[[]]])}('),False)
        assert_equal(sol('[{{{(())}}}]((()))'),True)
        assert_equal(sol('[[[]])]'),False)
        print('ALL TEST CASES PASSED')
        
# Run Tests

t = TestBalanceCheck()
print(t.test(balance_check))