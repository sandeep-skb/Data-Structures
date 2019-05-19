# Create a Node.
class Node:
  def __init__(self, data):
    self.data = data
    self.nextval = None

print("Creating Nodes:\n 'e1 = Node(<data>)'")
print()
e1 = Node(1)
e2 = Node(2)
print("connecting one Node to another Node:\n node1.nextval = node2")
print()
e1.nextval = e2
print("Accessing e1.data: ", e1.data)
print("Accessing e2 data from e1.nextval.data: ", e1.nextval.data)
