# Singly Linked list with deletion:
# At beginning of the LL
# At End of the LL
# At position X of the LL

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
    print()

  
  def delete_AtBeg(self):
    self.headnode = self.headnode.nextnode

  def delete_AtEnd(self):
    node = self.headnode
    if node == None:
      print("This is an empty node!!")
      return
    elif node.nextnode == None:
      print("This LL has only one element. Removing that!")
      self.headnode = None
      return
    
    while node.nextnode.nextnode != None:
      node = node.nextnode
    # At the end of the LL. Now delete the node.
    node.nextnode = None
  
  def delete_AtX(self, loc):
    count = 0
    node = self.headnode
    if loc == 0:
      self.delete_AtBeg()
      return
    while count != loc-1:
      if node.nextnode.nextnode == None:
        print("Sorry the node does not exist at location: {}, please provide a valid location.".format(loc))
        return
      node = node.nextnode
      count += 1
    # Insert the new node.
    node.nextnode = node.nextnode.nextnode

print("Creating Node:\n <node_name> = Node(<data>)")
e1 = Node("Monday")
e2 = Node("Tuesday")
print("Linking to the next node:\n node1.nextval = node2")
e1.nextnode = e2
e3 = Node("Wednesday")
e2.nextnode = e3
e4 = Node("Thursday")
e3.nextnode = e4
e5 = Node("Friday")
e4.nextnode = e5

print("Creating a head node for the singly linked list: \n head = SLinkedList()")
head = SLinkedList()
print("Assigning node to the head node:\n head.headval = <node>\n")
head.headnode = e1
print("Traversing through the LL:")
head.print_ll()


### Deleting AT BEGINNING
print("Deleting Monday at the beginning of the LL:\n 'head.delete_AtBeg()'\n")
head.delete_AtBeg()
print("Traversing:")
head.print_ll()

### INSERT AT END
print("Deleting Friday at the end of the LL:\n 'head.delete_AtEnd()'\n")
head.delete_AtEnd()
print("Traversing:")
head.print_ll()

### INSERTING AT POS: X
print("Deleting wednesday at loc {} of the LL:\n 'head.insert_AtX(1)'\n")
head.delete_AtX(0)
print("Traversing:")
head.print_ll()
