"""
Implement inorder traversal in O(1) space complexity

Assume every node have its parent address/info
Time Complexity  : O(n)
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

def inorder_traversal(root):
	
	current_node  = root
	previous_node = None
	next_node     = None
	result        = []
	
	while current_node:
		
		if previous_node is current_node.parent: # Traversing down the tree
			if current_node.left:
				next_node = current_node.left

			else: # No left child 
				result.append(current_node.data)
				
				# Done with all left children. So move right or UP
				next_node = current_node.right or current_node.parent

		elif previous_node is current_node.left: # Moved up from left child to parent
			result.append(current_node.data)

			# Done with all left children. So move right or UP
			next_node = current_node.right or current_node.parent


		else : # Done with both left and right subtrees. So move up
			next_node = current_node.parent


		previous_node, current_node = current_node, next_node

	return result


if __name__ == '__main__':

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

	print(inorder_traversal(root))	
