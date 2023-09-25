# Anagram Check
# Problem
# Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

# For example:

# "public relations" is an anagram of "crap built on lies."

# "clint eastwood" is an anagram of "old west action"

# Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "o d g".



# Solution 1: Sort the strings and compare them

def anagram(s1, s2):
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()
  return sorted(s1) == sorted(s2)


print(anagram('dog','god'))






# Solution 2: Count the number of each letter in each string and compare them

def anagram2(s1, s2):
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()

  if len(s1) != len(s2):
    return False

  s1dic = {}
  s2dic = {}
  
  for letter in s1:
    if letter in s1dic:
      s1dic[letter] +=1
    else:
      s1dic[letter] = 1
  
  for letter in s2:
    if letter in s2dic:
      s2dic[letter] +=1
    else:
      s2dic[letter] = 1

  return s1dic == s2dic

print(anagram2('dog','god'))

# Testing below

from nose.tools import assert_equal

class AnagramTest(object):
    
    def test(self,sol):
        assert_equal(sol('go go go','gggooo'),True)
        assert_equal(sol('abc','cba'),True)
        assert_equal(sol('hi man','hi     man'),True)
        assert_equal(sol('aabbcc','aabbc'),False)
        assert_equal(sol('123','1 2'),False)
        print("ALL TEST CASES PASSED")

# Run Tests
t = AnagramTest()
t.test(anagram)
t.test(anagram2)