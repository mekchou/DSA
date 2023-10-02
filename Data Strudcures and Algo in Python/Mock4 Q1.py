# first sort the list asc
# use two pointer, generate a loop to sum most left and right int, if smaller than target, move left pointer to right, if larget, move right to left, if match, return true

def twoSum(intList, target):
  leftPointer = 0
  rightPointer = len(intList) - 1
  matchTarget = False
  sumResult = None
  intList.sort()

  if len(intList) == 1 and intList[0] == target:
    matchTarget = True

  while leftPointer != rightPointer  and not matchTarget:
    sumResult = intList[leftPointer] + intList[rightPointer]
    if sumResult < target:
      leftPointer += 1
    elif sumResult > target:
      rightPointer -= 1
    else:
      matchTarget = True
  
  return matchTarget

intList = [5,4,9,3,3]
print(twoSum(intList, 6))


def twoSum2(intList, target):
  seen = set()

  for num in intList:
    num2 = target - num
    if num2 in seen:
      return True
    seen.add(num)
  return False
intList = [5,4,9,3,3]
print(twoSum2(intList, 10))