class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def reverseLevelOrder(node):
  if node == None:
    print("Node is empty, illegal input")
    return
  
  q = [node]
  s = []
  while(len(q) != 0):
    tmp = q.pop(0)
    if tmp.right != None:
      q.append(tmp.right)
    if tmp.left != None:
      q.append(tmp.left)
    
    s.append(tmp)
  
  while(len(s) != 0):
    tmp = s.pop()
    print(tmp.data, end=" ")
  print()
  

def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  t1.left.right = Node(5)
  t1.right.left = Node(6)
  t1.right.right = Node(7)

  print("Printing Reverse Level Order: ")
  reverseLevelOrder(t1)

if __name__ == "__main__":
  main()
