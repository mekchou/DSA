# Interative Version

def binary_search(arr, ele):

  first = 0
  last = len(arr) -1
  found = False

  while first <= last and not found:
    mid =(first + last) // 2

    if arr[mid] == ele:
      found = True
    else:
      if ele < arr[mid]:
        last = mid -1
      else:
        first = mid + 1
  return found

arr = [1,2,3,4,5,6,7,8,10,9]
arr.sort()
print(binary_search(arr, 31))


# Recursive Version

def binary_search_rec(arr, ele):
  if len(arr) == 0:
    return False
  else:
    mid = len(arr) // 2
    if arr[mid] == ele:
      return True
    elif arr[mid] < ele:
      return binary_search_rec(arr[mid+1:],ele)
    else:
      return binary_search_rec(arr[:mid], ele)

print(binary_search_rec(arr,9))
