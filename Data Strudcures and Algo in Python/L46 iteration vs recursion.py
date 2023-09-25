def calculate_itr(n):
  while n > 0:
    k = n**2
    print(k)
    n = n - 1

def calculate_rec(n):
  if n > 0:
    k = n**2
    print(k)
    calculate_rec(n-1)


calculate_itr(5)
calculate_rec(5)