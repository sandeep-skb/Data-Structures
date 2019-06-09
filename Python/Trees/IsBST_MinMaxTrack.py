'''
check if the tree is BST.
This is the min max tracking approach.
'''

class Node:
  def __init__(self, data):
    self.data = data
    self.right = None
    self.left = None

def insert(node, data):
  if node == None:
    return Node(data)
  elif (data < node.data):
    node.left = insert(node.left, data)
  else:
    node.right = insert(node.right, data)
  
  return node

def inorder(node):
  if node == None:
    return
  
  if node.left != None:
    inorder(node.left)
  print(node.data, end=" ")
  if node.right != None:
    inorder(node.right)

def isBSTUtil(node, min_val, max_val):
  if node == None:
    return True
  else:
    return (node.data > min_val and node.data < max_val and (isBSTUtil(node.left, min_val, node.data) and isBSTUtil(node.right, node.data, max_val)))

def isBST(node):
  if node == None:
    return True
  else:
    min_val = -1
    max_val = 100
    return (node.data > min_val and node.data < max_val and (isBSTUtil(node.left, min_val, node.data) and isBSTUtil(node.right, node.data, max_val)))

  

# driver code
def main():
  root = None
  root = insert(root, 50) 
  root = insert(root, 30) 
  root = insert(root, 20) 
  root = insert(root, 40) 
  root = insert(root, 70) 
  root = insert(root, 60) 
  root = insert(root, 80) 
    
  print ("Inorder traversal of the given tree")
  inorder(root) 
  print()

  print("Is BST: ", isBST(root))
   
   

if __name__ == "__main__":
  main()
