class node(object):

  def __init__(self,value):
    
    self.value = value
    self.nextnode = None

a = node(1)
b = node(2)
c = node(3)

a.nextnode = b
b.nextnode = c

print(a.value)
print(a.nextnode)
print(a.nextnode.value)