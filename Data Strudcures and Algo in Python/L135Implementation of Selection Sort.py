def selection_sort(arr):
  
  for fillslot in range(len(arr)-1, 0, -1):
    positionOfMax = 0

    for location in range(1, fillslot+1):
      if arr[location] > arr[positionOfMax]:
        positionOfMax = location
    
    temp = arr[fillslot]
    arr[fillslot] = arr[positionOfMax]
    arr[positionOfMax] = temp

arr = [5,8,3,10,1]
# print(arr)
# print(list(range(len(arr)-1,0,-1)))