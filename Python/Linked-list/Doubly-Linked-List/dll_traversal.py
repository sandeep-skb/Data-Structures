## Doubly Linked list Traversal

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DLL:
  def __init__(self, node):
    self.headnode = node
  
  def print_dll(self):
    node = self.headnode
    while(node != None):
      print(node.data)
      node = node.next


e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e1.next = e2
e2.prev = e1

e2.next = e3
e3.prev = e2

dll = DLL(e1)
dll.print_dll()
