class Node:

	node_value = 0
	left_node = None
	right_node = None

	def __init__(self,value=0,left=None,right=None):
		self.node_value = value
		self.left_node = left
		self.right_node = right

	def __lt__(self,other):		
		return self.getValue() < other.getValue()

	def __gt__(self,other):
		return self.getValue() > other.getValue()

	def __str__(self):
		return str(self.node_value)

	def setValue(self,value):
		self.node_value = value

	def getValue(self):
		return self.node_value

	def setLeft(self, left):
		self.node_left = left

	def getLeft(self):
		return self.node_left

	def setRight(self,right):
		self.node_right = right

	def insert(self,node):
		if node <= self.node_left and self.node_left == None:
			self.node_left = node
 		elif node >self.node_right  and self.node_right == None:
			self.node_right = node
		elif node <= slef.node_left:
			self.node_left.insert(node)
		elif node > self.node_right:
			self.node_right.insert(node)
 


class BinaryTree:
	
	root = None

	def __init__(self,rootNode=None):
		self.root = rootNode

	def traverse(self,node="a"):
		if(self.root==None):
			print("Empty Tree")
			return
			
		if(node==None):
			return

		if(node.getLeft()==None and node.getRight==None):
			print(node.getValue())

		self.traverse(node.getLeft())
		self.traverse(node.getRight())
			
	
		print(node)
	
	def setRoot(self,node):
		self.root = node

	def hasRoot(self):
		ret = False
		
		if(self.root != None):
			ret = True

		return ret		
	
	

#main

x = [2,3,1,4,99,4]

b = BinaryTree()

for item in x:
	if(!b.hasRoot()):
		b=
b = BinaryTree(a)

b.traverse(a)


