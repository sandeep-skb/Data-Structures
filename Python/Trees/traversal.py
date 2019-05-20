# This program has inorder, pre-order and post-order traversals of a binary tree.
class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


def inorder(node):
  if node.left != None:
    inorder(node.left)
  print(node.data, end=" ")
  if node.right != None:
    inorder(node.right)

def preorder(node):
  print(node.data, end=" ")
  if node.left != None:
    preorder(node.left)
  if node.right != None:
    preorder(node.right)

def postorder(node):
  if node.left != None:
    postorder(node.left)
  if node.right != None:
    postorder(node.right)
  print(node.data, end=" ")


# Driver code 
root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5) 
print ("Preorder traversal of binary tree is:")
preorder(root)
print() 

print ("Inorder traversal of binary tree is:")
inorder(root)
print() 

print ("Postorder traversal of binary tree is:")
postorder(root)
print() 
