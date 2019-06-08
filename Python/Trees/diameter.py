class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def height(node):
  if node == None:
    return 0
  return (max(height(node.left), height(node.right))+1)
  
def diameter(node):
  '''
  The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes. 
  The diagram below shows two trees each with diameter nine, the leaves that form the ends of a longest path are shaded 
  (note that there is more than one path in each tree of length nine, but no path longer than nine nodes).
  https://www.geeksforgeeks.org/diameter-of-a-binary-tree/
  '''
  
  
  
  if node == None:
    return 0
  lheight = height(node.left)
  rheight = height(node.right)

  ldiameter = diameter(node.left)
  rdiameter = diameter(node.right)

  #diameter will be the max of the following:
  #1. diameter through the root Node
  #2. diameter of the left subtree
  #3. diamter of the right subtree
  return(max((lheight+rheight+1), max(ldiameter, rdiameter)))

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

  print("Printing the diameter of tree: ")
  print(diameter(t1))

if __name__ == "__main__":
  main()
