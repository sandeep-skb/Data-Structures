class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def preOrder(node):
  if node != None:
    print(node.data)
    preOrder(node.left)
    preOrder(node.right)

def findMax(node):
  if node == None:
    return -1
  
  return max(node.data, max(findMax(node.left), findMax(node.right))) 

def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  t1.left.right = Node(5)
  t1.right.left = Node(6)
  t1.right.right = Node(7)

  preOrder(t1)
  print()
  print("Maximum value of the tree is : ", findMax(t1))

if __name__ == "__main__":
  main()
