def calculate_headrec(n):
  if n > 0:
    calculate_headrec(n-1)
    k = n**2
    print(k)
def calculate_tailrec(n):
  if n > 0:
    k = n**2
    print(k)
    calculate_tailrec(n-1)

print("This is head recursion")
calculate_headrec(5)
print("This is tail recursion")
calculate_tailrec(5)