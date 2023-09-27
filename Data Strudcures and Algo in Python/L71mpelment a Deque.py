class deque(object):

  def __init__(self):
    self.items = []

  def addFront(self,item):
    self.items.append(item)

  def addRear(self, item):
    self.items.insert(0,item)
  
  def removeFront(self):
    return self.items.pop()

  def removeRear(self):
    return self.items.pop(0)
  
  def isEmpty(self):
    return self.items == []
  
  def size(self):
    return len(self.items)

d = deque()
d.addFront('hello')
d.addRear('world')
print(d.size())
print(d.isEmpty())
print(d.removeFront() + ' ' + d.removeRear())
print(d.isEmpty())
print(d.size())
