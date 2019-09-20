import random

class LinkedListNode:

	def __init__(self, tree_node=None, next=None):
		self.tree_node = tree_node
		self.next = next

	def get_tree_node(self):
		return self.tree_node

	def get_next(self):
		return self.next

	def set_next(self, new_tree_node):
		self.tree_node = new_tree_node


class Queue(LinkedListNode):

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def Enqueue(self, tree_node):
		queue_node = LinkedListNode(tree_node)

		if self.head is None and self.tail is None:
			self.head = queue_node
			self.tail = queue_node
		else:
			self.tail.set_next(queue_node)
			self.tail = self.tail.get_next()

	def Dequeue(self):
		if self.head is None:
			print("Queue non-existent.\n")
			return None

		pop_node = self.head
		self.head = self.head.get_next()
		if self.head is None:
			self.tail = None
		return pop_node.get_tree_node()

	def get_front(self):
		return self.head.get_tree_node()

	def is_empty(self):
		if self.head is None and self.tail is None:
			return True
		return False


class Stack(LinkedListNode):

	def __init__(self, top=None):
		self.top = top

	def Push(self, tree_node):
		stack_node = LinkedListNode(tree_node)

		if self.top is None:
			self.top = stack_node
		else:
			stack_node.set_next(self.top)
			self.top = stack_node

	def Pop(self):
		if self.top is None:
			print("Stack non-existent.\n")
			return None

		pop_node = self.top
		self.top = self.top.get_next()
		return pop_node.get_tree_node()

	def get_top(self):
		return self.top.get_tree_node()

	def is_empty(self):
		if self.top is None:
			return True
		return False


class TreeNode:

	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def get_data(self):
		return self.data

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

	def set_left(self, new_tree_node):
		self.left = new_tree_node

	def set_right(self, new_tree_node):
		self.right = new_tree_node


class BinaryTree(TreeNode):
	insertion_queue = Queue()

	def __init__(self, root=None):
		self.root = root
		
	def insert_node(self, data):
		tree_node = TreeNode(data)

		if self.root is None:
			self.root = tree_node
		else:
			front = self.insertion_queue.get_front()

			if front.get_left() is None:
				front.set_left(tree_node)
			elif front.get_right() is None:
				front.set_right(tree_node)

			if front.get_left() is not None and front.right() is not None:
				insertion_queue.Dequeue()

		insertion_queue.Enqueue(tree_node)

	def level_order_traversal(self):
		if self.root is None:
			print("Tree non-existent.\n")
			return

		traversal_queue = Queue()
		traversal_queue.Enqueue(self.root)

		while traversal_queue.is_empty() is False:
			tree_node = traversal_queue.Dequeue()

			print(tree_node.get_data())

			if tree_node.get_left() is not None:
				traversal_queue.Enqueue(tree_node.get_left())
			if tree_node.get_right() is not None:
				traversal_queue.Enqueue(tree_node.get_right())

	def preorder_traversal_recursive(self)
