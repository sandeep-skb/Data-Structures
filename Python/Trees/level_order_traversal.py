class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def levelOrderTraversal(node):
  q = []
  q.append(node)
  while(len(q) != 0):
    node = q.pop(0)
    print(node.data, end=" ")
    if node.left != None:
      q.append(node.left)
    if node.right != None:
      q.append(node.right)
    




# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)

levelOrderTraversal(root)
