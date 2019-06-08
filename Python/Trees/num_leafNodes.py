class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def leafNode(node):
  q = [node]
  count = 0
  while(len(q) != 0):
    temp = q.pop(0)
    if (temp.left == None and temp.right == None):
      count += 1
    if (temp.left != None):
      q.append(temp.left)
    if (temp.right != None):
      q.append(temp.right)
  
  return count

  
  

def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  t1.left.right = Node(5)
  t1.right.left = Node(6)
  t1.right.right = Node(7)
  '''
       1
    /    \
   2      3
  / \    / \
 4   5  6   7
       
      
  '''

  print("Printing # of leaf nodes in the tree: ")
  print(leafNode(t1))

if __name__ == "__main__":
  main()
