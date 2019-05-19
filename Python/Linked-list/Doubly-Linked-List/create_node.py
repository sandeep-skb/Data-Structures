## Doubly Linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

e2 = Node("Tue")
e1 = Node("Mon")
e1.next = e2
e2.prev = e1

print("e1.data: ", e1.data)
print("e1.next.data: ", e1.next.data)
print("e2.prev.data: ", e2.prev.data)
