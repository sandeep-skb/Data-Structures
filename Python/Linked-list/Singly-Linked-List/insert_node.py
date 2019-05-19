# Singly Linked list with Insertion:
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

  
  def insert_AtBeg(self, data):
    new_node = Node(data)
    new_node.nextnode = self.headnode
    self.headnode = new_node

  def insert_AtEnd(self, data):
    new_node = Node(data)
    node = self.headnode
    while node.nextnode != None:
      node = node.nextnode
    # At the end of the LL. Now attach the new node here.
    node.nextnode = new_node
  
  def insert_AtX(self, loc, data):
    new_node = Node(data)
    node = self.headnode
    count = 0
    if loc == 0:
      self.insert_AtBeg(data)
      return
    while count != loc-1:
      if node.nextnode == None:
        print("Sorry the node does not exist at location: {}, please provide a valid location.".format(loc))
        return
      node = node.nextnode
      count += 1
    # Insert the new node.
    new_node.nextnode = node.nextnode
    node.nextnode = new_node


print("Creating Node:\n <node_name> = Node(<data>)")
e1 = Node("Monday")
e2 = Node("Tuesday")
print("Linking to the next node:\n node1.nextval = node2")
e1.nextnode = e2
e3 = Node("Wednesday")
e2.nextnode = e3

print("Creating a head node for the singly linked list: \n head = SLinkedList()")
head = SLinkedList()
print("Assigning node to the head node:\n head.headval = <node>\n")
head.headnode = e1
print("Traversing through the LL:")
head.print_ll()


### INSERT AT BEGINNING
print("Inserting sunday at the beginning of the LL:\n 'head.insert_AtBeg('Sunday')'\n")
head.insert_AtBeg("Sunday")
print("Traversing:")
head.print_ll()

### INSERT AT END
print("Inserting Thrusday at the end of the LL:\n 'head.insert_AtEnd('Thursday')'\n")
head.insert_AtEnd("Thrusday")
print("Traversing:")
head.print_ll()

### INSERTING AT POS: X
print("Inserting Friday at loc {} of the LL:\n 'head.insert_AtX(2, 'Friday')'\n")
head.insert_AtX(2, "Friday")
print("Traversing:")
head.print_ll()
