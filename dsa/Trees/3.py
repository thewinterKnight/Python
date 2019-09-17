# How do you perform inorder traversal in a binary tree?

import random
import copy

class LinkedListNode:

	def __init__(self, tree_node=None, next=None):
		self.tree_node = tree_node
		self.next = next

	def get_tree_node(self):
		return self.tree_node

	def get_next(self):
		return self.next

	def set_next(self, new_tree_node):
		self.next = new_tree_node


class Queue(LinkedListNode):

	def __init__(self, head=None, tail=None):
		self.head = head
		self.tail = tail

	def Enqueue(self, new_tree_node):
		queue_node = LinkedListNode(new_tree_node)

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

	def Push(self, new_tree_node):
		stack_node = LinkedListNode(new_tree_node)

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

	def __init__(self, root=None):
		self.root = root

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



	def inorder_traversal_recursive(self):
		if self.root is None:
			print("Tree non-existent.\n")
			return

		self.inorder_recursive_util(self.root)

	def inorder_recursive_util(self, tree_node):
		if tree_node is None:
			return

		self.inorder_recursive_util(tree_node.get_left())
		print(tree_node.get_data())
		self.inorder_recursive_util(tree_node.get_right())

	def inorder_traversal_iterative(self):
		if self.root is None:
			print("Tree non-existent.\n")
			return

		traversal_stack = Stack()
		traversal_stack.Push(self.root)

		while traversal_stack.is_empty() is False:
			tree_node = traversal_stack.Pop()

			if tree_node.get_right() is not None:
				traversal_stack.Push(tree_node.get_right())
			print(tree_node.get_data())
			if tree_node.get_left() is not None:
				traversal_stack.Push(tree_node.get_left())



def insert_node(binary_tree, data, insertion_queue):
	insert_tree_node = TreeNode(data)

	if binary_tree.root is None:
		binary_tree.root = insert_tree_node
	else:
		front = insertion_queue.get_front()

		if front.get_left() is None:
			front.set_left(insert_tree_node)
		elif front.get_right() is None:
			front.set_right(insert_tree_node)

		if front.get_left() is not None and front.get_right() is not None:
			insertion_queue.Dequeue()

	insertion_queue.Enqueue(insert_tree_node)


if __name__ == "__main__":
	binary_tree = BinaryTree()
	queue = Queue()

	arr = list(range(1, 12))
	random.shuffle(arr)

	print(arr)

	print("Converting to a complete binary tree...\n\n")

	for i in arr:
		insert_node(binary_tree, i, queue)

	print("Level Order Traversal :")
	binary_tree.level_order_traversal()

	print("\n\nInOrder Traversal(Recursive) :")
	binary_tree.inorder_traversal_recursive()

	print("\n\nInOrder Traversal(Iterative) :")
	binary_tree.inorder_traversal_iterative()