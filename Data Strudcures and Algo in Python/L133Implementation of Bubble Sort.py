def bubble_sort(arr):
  for n in range(len(arr)-1,0,-1):
    for k in range(n):
      if arr[k] > arr[k+1]:
        # temp = arr[k]
        # arr[k] = arr[k+1]
        # arr[k+1] = temp
        arr[k], arr[k+1] = arr[k+1], arr[k]

arr = [5,3,7,2]
# print(list(range(len(arr)-1,0,-1)))
bubble_sort(arr)
print(arr)