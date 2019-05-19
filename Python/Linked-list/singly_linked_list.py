# Singly Linked list

class Node:
  def __init__(self, data):
    self.data = data
    self.nextnode = None


class SLinkedList:
  def __init__(self):
    self.headnode = None
  
  def print_ll(self):
    node = self.headnode
    while node != None:
      print(node.data)
      node = node.nextnode

print("Creating Node:\n <node_name> = Node(<data>)")
e1 = Node("monday")
e2 = Node("teusday")
print("Linking to the next node:\n node1.nextval = node2")
e1.nextnode = e2
e3 = Node("wednesday")
e2.nextnode = e3

print("Creating a head node for the singly linked list: \n head = SLinkedList()")
head = SLinkedList()
print("Assigning node to the head node:\n head.headval = <node>\n")
head.headnode = e1
print("Traversing through the LL:")
head.print_ll()
