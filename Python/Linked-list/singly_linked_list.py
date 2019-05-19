# Singly Linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.nextval = None


class SLinkedList:
  def __init__(self):
    self.headnode = None
  
  def print_ll(self):
    node = self.headnode
    while node != None:
      print(node.data)
      node = node.nextval

print("Creating Node:\n <node_name> = Node(<data>)")
e1 = Node(1)
e2 = Node(2)
print("Linking to the next node:\n node1.nextval = node2")
e1.nextval = e2
e3 = Node(3)
e2.nextval = e3

print("Creating a head node for the singly linked list: \n head = SLinkedList()")
head = SLinkedList()
print("Assigning node to the head node:\n head.headval = <node>")
head.headnode = e1
head.print_ll()
