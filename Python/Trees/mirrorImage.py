# Algorithm to convert the tree to its mirror.
class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def mirrorBT(node):
  if not node:
    return
  mirrorBT(node.left)
  mirrorBT(node.right)
  node.left, node.right = node.right, node.left
  print("node.data", node.data)
  if node.left:
    print("left: ", node.left.data)
  if node.right:
    print("right: ", node.right.data)

def preorder(node):
  if not node: return
  print(node.data, end= " ")
  preorder(node.left)
  preorder(node.right)



def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  t1.left.right = Node(5)
  t1.right.left = Node(6)
  t1.right.right = Node(7)
  t1.right.right.right = Node(9)
  '''
       1
    /    \
   2      3
  / \    / \
 4   5  6   7
             \
              9       
      
  '''

  print("sequence before inverting: ")
  preorder(t1)
  print()
  mirrorBT(t1)
  print("sequence after inverting: ")
  preorder(t1)
if __name__ == "__main__":
  main()
