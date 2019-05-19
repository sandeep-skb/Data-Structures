## Doubly Linked list Insertion

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
    print()

  ## Insert at Beginning
  def insert_AtBeg(self, data):
    new_node = Node(data)
    self.headnode.prev = new_node
    new_node.next = self.headnode
    self.headnode = new_node
  
  ## Insert at End
  def insert_AtEnd(self, data):
    new_node = Node(data)
    node = self.headnode
    while node.next != None:
      node = node.next
    
    #At the end, insert the node here
    node.next = new_node
    new_node.prev = node

  def insert_AtX(self, loc, data):
    new_node = Node(data)
    node = self.headnode
    count = 0
    if loc == 0:
      self.insert_AtBeg(data)
      return 

    while count != loc:
      if node == None:
        print("Please enter a valid location!")
        return
      node = node.next
      count += 1
    
    new_node.next = node
    new_node.prev = node.prev
    node.prev.next = new_node
    node.prev = new_node


e1 = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e1.next = e2
e2.prev = e1

e2.next = e3
e3.prev = e2

dll = DLL(e1)
dll.print_dll()

print("Inserting Sun at the beginning of the DLL")
dll.insert_AtBeg("Sun")
dll.print_dll()

print("Inserting Thu at the End of the DLL")
dll.insert_AtEnd("Thu")
dll.print_dll()

print("Inserting Fri at the pos 2 of the DLL")
dll.insert_AtX(3, "Fri")
dll.print_dll()
