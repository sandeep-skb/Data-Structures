class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def maxDepth(node):
  if node == None:
    return -1
  
  return(max(maxDepth(node.left), maxDepth(node.right))+1)

def minDepth(node):
  if node == None:
    return -1
  
  return (min(maxDepth(node.left), maxDepth(node.right)) + 1)
  

def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  t1.left.right = Node(5)
  t1.right.left = Node(6)
  t1.right.left.left = Node(8)
  '''
       1
    /    \
   2      3
  / \    /
 4   5  6
       /
      8
  '''

  print("Printing Min depth of the tree: ")
  print(minDepth(t1))

if __name__ == "__main__":
  main()
