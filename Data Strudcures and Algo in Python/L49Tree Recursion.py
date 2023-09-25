def calculate_treerec(n):
  if n > 0:
    calculate_treerec(n-1)
    k = n**2
    print(k)
    calculate_treerec(n-1)
# def calculate_tailrec(n):
#   if n > 0:
#     k = n**2
#     print(k)
#     calculate_tailrec(n-1)

print("This is head recursion")
calculate_treerec(3)
# print("This is tail recursion")
# calculate_tailrec(5)