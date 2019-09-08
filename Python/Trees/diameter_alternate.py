class Node: 
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None


def diameter(root):
  def helper(root):
      if not root:
          return [0,0]
      ldia, lheight = helper(root.left)
      rdia, rheight = helper(root.right)
      return [max(ldia, rdia, (1+lheight+rheight)), 1+max(lheight, rheight)]
  
  dia, height = helper(root)
  return dia 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
print ("Diameter of given binary tree is ", diameter(root))
