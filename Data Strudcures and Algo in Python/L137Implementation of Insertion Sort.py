def insertion_sort(arr):
  for i in range(1,len(arr)):
    currentvalue = arr[i]
    position = i

    while position > 0 and arr[position-1] > currentvalue:
      arr[position] = arr[position-1]
      position = position-1
    arr[position] = currentvalue
    
arr= [4,6,2,7,4,1,9,11,23,13,2]
insertion_sort(arr)
print(arr)