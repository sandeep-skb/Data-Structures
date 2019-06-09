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

def findMinNode(node):
  if node == None:
    return node
  elif node.left != None:
    return (findMinNode(node.left))
  else:
    return node

def deleteNode(node, data):
  if node == None: 
    return None

  if data < node.data:
    node.left = deleteNode(node.left, data)
  elif data > node.data:
    node.right = deleteNode(node.right, data)
  else:
    if node.left == None:
      temp = node.right
      node = None
      return temp
    elif node.right == None:
      temp = node.left
      node = None
      return temp
    else:
      temp = findMinNode(node.right)
      node.data = temp.data
      node.right = deleteNode(node.right, temp.data)
  
  return node
  

# driver code
def main():
""" Let us create following BST 
              50 
           /     \ 
          30      70 
         /  \    /  \ 
       20   40  60   80 """
  
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

  print ("Delete 70")
  root = deleteNode(root, 70) 
  print ("Inorder traversal of the modified tree")
  inorder(root) 

if __name__ == "__main__":
  main()
