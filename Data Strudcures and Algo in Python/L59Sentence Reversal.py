def rev_word(s):
  return " ".join(reversed(s.split()))


print(rev_word('Hi John,   are you ready to go?'))

print(rev_word('    space before'))

# interview solution, to do it properly in array
def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                # keep adding until hitting space
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        # keep adding until hitting non-space
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):
    
    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print("ALL TEST CASES PASSED")
        
# Run and test
t = ReversalTest()
t.test(rev_word)
t.test(rev_word3)