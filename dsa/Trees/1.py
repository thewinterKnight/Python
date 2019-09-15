# How is a complete binary search tree implemented?

import random


class QueueNode:

	def __init__(self, tree_node=None, next=None):
		self.tree_node = tree_node
		self.next = next

	def get_tree_node(self):
		return self.tree_node

	def get_next(self):
		return self.next

	def set_next(self, new_node):
		self.next = new_node


class Queue(QueueNode):

	def __init__(self, head=None, tail=None):
		# super().__init__()
		self.head = head
		self.tail = tail

	def Enqueue(self, tree_node):
		new_node = QueueNode(tree_node)

		if self.tail is None and self.head is None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.set_next(new_node)
			self.tail = self.tail.get_next()

	def get_front(self):
		return self.head

	def Dequeue(self):
		if self.head is None:
			return None

		pop_node = self.head
		self.head = self.head.get_next()
		if self.head is None:
			self.tail = None

		return pop_node.get_tree_node()

	def is_empty(self):
		if self.head is None and self.tail is None:
			return True
		else:
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

	def set_left(self, left_node):
		self.left = left_node

	def set_right(self, right_node):
		self.right = right_node


class BinaryTree(TreeNode):

	def __init__(self, root=None):
		# super().__init__()
		self.root = root

	def level_order_traversal(self):
		if self.root is None:
			print("Tree does not exist\n")
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


def insert_node(binary_tree, data, queue):
	new_node = TreeNode(data)

	if binary_tree.root is None:
		binary_tree.root = new_node
	else:
		queue_front = queue.get_front()		# queue_front is a tree node that was put in the queue
		tree_node = queue_front.get_tree_node()

		if tree_node.get_left() is None:
			tree_node.set_left(new_node)
		elif tree_node.get_right() is None:
			tree_node.set_right(new_node)

		if tree_node.get_left() is not None and tree_node.get_right() is not None:
			queue.Dequeue()

	queue.Enqueue(new_node)


if __name__ == "__main__":
	binary_tree = BinaryTree()
	queue = Queue()

	arr = list(range(1, 12))
	random.shuffle(arr)

	print(arr)

	print("Converting to a complete binary tree...\n\n")

	for i in arr:
		insert_node(binary_tree, i, queue)
	binary_tree.level_order_traversal()





