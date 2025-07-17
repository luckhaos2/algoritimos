class Node:
    def __init__ (self,val):
        self.val = val
        next = None

class List:
  def __init__(self):
    self.head = None
    self.size = 0

  def push(self,val):
    data = Node(val)
    data.next = self.head
    self.head = data
    self.size += 1
    return self.head.val
        

add = List().push()

print(add)