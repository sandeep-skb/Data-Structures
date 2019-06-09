class Node:
  def __init__(self, val):
    self.data = val
    self.left = None
    self.right = None

def verticalSumInBinaryTree(node, idx, myhash):
  if node != None:
    if idx in myhash.keys():
      myhash[idx].append(node.data)
    else:
      myhash[idx] = [node.data]

    if node.left != None:
      myhash = verticalSumInBinaryTree(node.left, idx-1, myhash)
    if node.right != None:
      myhash = verticalSumInBinaryTree(node.right, idx+1, myhash)
    
    return myhash


def verticalSumInBinaryTree_main(node):
  myhash = {}
  myhash = verticalSumInBinaryTree(node, 0, myhash)
  for k in sorted(myhash.keys()):
    print("Vertical sum of {} is {}".format(k, sum(myhash[k])))


def main():
  t1 = Node(1)
  t1.left = Node(2)
  t1.right = Node(3)
  t1.left.left = Node(4)
  #t1.left.left.left = Node(9)
  #t1.left.left.right = Node(10)
  
  t1.left.right = Node(5)
  #t1.left.right.left = Node(11)
  #t1.left.right.right = Node(12)

  t1.right.left = Node(6)
  #t1.right.left.left = Node(13)
  #t1.right.left.right = Node(14)
  
  t1.right.right = Node(7)
  #t1.right.right.left = Node(15)
  #t1.right.right.right = Node(16)
  '''
            1
         /     \
        2       3
      /  \     /  \
    4     5   6     7
 
  '''

  print("Printing in zigzag pattern: ")
  verticalSumInBinaryTree_main(t1)
  print()

if __name__ == "__main__":
  main()
