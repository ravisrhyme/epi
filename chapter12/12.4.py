"""
Compute the LCA,optimising for close ancestors

Time Complexity  : O(h) h is min height between any of nodes to root.
Space Complexity : O(1)

"""
__author__  = "Ravi Kiran Chadalawada"
__email__   = "rchadala@usc.edu"
__credits__ = ["Elements of Programming Interviews"]
__status__  = "Prototype"



class node():
	def __init__(self,value):
		self.data = value
		self.left = None
		self.right = None
		self.parent = None

def find_lca(node_0,node_1):

	temp_0 = node_0
	temp_1 = node_1

	nodes_in_path_to_root = set()
	while temp_0 or temp_1:
		if temp_0:
			if temp_0 in nodes_in_path_to_root:
				return temp_0

			nodes_in_path_to_root.add(temp_0)	
			temp_0 = temp_0.parent


		if temp_1:
			if temp_1 in nodes_in_path_to_root:
				return temp_1

			nodes_in_path_to_root.add(temp_1)
			temp_1 = temp_1.parent

	return None

if __name__=='__main__':

	root = node(8)
	root.left = node(6)
	root.left.parent = root
	root.right = node(10)
	root.right.parent = root

	root.left.left = node(5)
	root.left.left.parent = root.left
	root.left.right = node(7)
	root.left.right.parent = root.left

	root.right.left = node(9)
	root.right.left.parent = root.right
	root.right.right = node(11)
	root.right.right.parent = root.right

	print(find_lca(root.left,root.right.left).data)
