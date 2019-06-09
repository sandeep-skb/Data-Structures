class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def maxLevelSum(node):
  q = [node]
  result = node.data
  while(len(q) != 0):
    max_val = 0
    count = len(q)
    while(count != 0):
      temp = q.pop(0)
      max_val += temp.data 
      if (temp.left != None):
        q.append(temp.left)
      if (temp.right != None):
        q.append(temp.right)
      count -= 1
    result = max(result, max_val)
  return result


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

  print("Printing the level order max sum: ")
  print(maxLevelSum(t1))

if __name__ == "__main__":
  main()
