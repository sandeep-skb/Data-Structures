class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def printZigZag(node):
  stack1 = [node]
  stack2 = []
  use_stack1 = 1
  while((use_stack1==1 and len(stack1)!= 0) or (use_stack1==0 and len(stack2)!= 0)):
    if (use_stack1 == 1):
      temp = stack1.pop(-1)
      print(temp.data, end = " ")
      if (temp.left != None):
        stack2.append(temp.left)
      if (temp.right != None):
        stack2.append(temp.right)
      if (len(stack1) == 0):
        use_stack1 = 0
    else:
      temp = stack2.pop(-1)
      print(temp.data, end=" ")
      if (temp.right != None):
        stack1.append(temp.right)
      if (temp.left != None):
        stack1.append(temp.left)
      if (len(stack2) == 0):
        use_stack1 = 1

def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  t1.left.left.left = Node(9)
  t1.left.left.right = Node(10)
  
  t1.left.right = Node(5)
  t1.left.right.left = Node(11)
  t1.left.right.right = Node(12)

  t1.right.left = Node(6)
  t1.right.left.left = Node(13)
  t1.right.left.right = Node(14)
  
  t1.right.right = Node(7)
  t1.right.right.left = Node(15)
  t1.right.right.right = Node(16)
  '''
              1
         /         \
        2           3
      /  \        /  \
    4     5      6     7
   / \   / \   / \    / \        
  9  10 11 12 13  14 15  16 
  '''

  print("Printing in zigzag pattern: ")
  printZigZag(t1)
  print()

if __name__ == "__main__":
  main()
