
#have a set to record what shows up already
# create a loop to first check if exists in set, if not exists, append to string, else, do nothing. outside of the if, add element to the set


def removeDuplicate(inputString):
  occurrences = set()
  outputString = ""

  for char in inputString:
    if char not in occurrences:
      outputString = outputString + char
      occurrences.add(char)
  return outputString


inputString = "tree traversal"
print(removeDuplicate(inputString))