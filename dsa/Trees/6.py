# Implement a threaded binary tree.

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
			print('Queue non-existent.\n')
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
			print('Stack non-existent.\n')
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

	def __init__(self, data=None, left=None, right=None, is_right_threaded=False):
		self.data = data
		self.left = left
		self.right = right
		self.is_right_threaded = is_right_threaded

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

	def get_right_thread_status(self):
		return is_right_threaded

	def set_right_thread_status(self, status):
		self.is_right_threaded = status


class BinaryTree(TreeNode):
	insertion_queue = Queue()

	def __init__(self, root=None):
		self.root = root

	def insert_node(self, data):
		tree_node = TreeNode(data)

		if self.root is None:
			self.root = tree_node
			self.insertion_queue.Enqueue(self.root)
		else:
			front_tree_node = self.insertion_queue.get_front()

			if front_tree_node.get_left() is None:
				front_tree_node.set_left(tree_node)
			elif front_tree_node.get_right() is None:
				front_tree_node.set_right(tree_node)

			if front_tree_node.get_left() is not None and front_tree_node.get_right() is not None:
				self.insertion_queue.Dequeue()

		self.insertion_queue.Enqueue(tree_node)

	def fetch_tree_node(self, node_data):
		if self.root is None:
			print('Tree non-existent.\n')
			return None

		traversal_stack = Stack()
		traversal_node = self.root
		while traversal_node is not None or traversal_stack.is_empty() is False:
			while traversal_node is not None:
				traversal_stack.Push(traversal_node)
				traversal_node = traversal_node.get_left()

			traversal_node = traversal_stack.Pop()
			if traversal_node.get_data() == node_data:
				return traversal_node
			traversal_node = traversal_node.get_right()

	def level_order_traversal(self):
		if self.root is None:
			print('Tree non-existent.\n')
			return None

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
			print('Tree non-existent.\n')
			return None

		self.inorder_traversal_recursive_util(self.root)

	def inorder_traversal_recursive_util(self, node):
		if node is None:
			return

		self.inorder_traversal_recursive_util(node.get_left())
		print(node.get_data())
		self.inorder_traversal_recursive_util(node.get_right())

	def inorder_predecessor(self, node_data):
		if self.root is None:
			print('Tree non-existent.\n')
			return None

		traversal_stack = Stack()
		traversal_node = self.root
		predecessor_node = None
		while traversal_node is not None or traversal_stack.is_empty() is False:
			while traversal_node is not None:
				traversal_stack.Push(traversal_node)
				traversal_node = traversal_node.get_left()

			traversal_node = traversal_stack.Pop()
			
			if traversal_node.get_data() == node_data:
                                if predecessor_node is not None:
                                        print('Inorder predecessor is : {}'.format(predecessor_node.get_data()))
                                else:
                                        print('Inorder predecessor does not exist.')
				return predecessor_node
			else:
				predecessor_node = traversal_node

			traversal_node = traversal_node.get_right()

	def inorder_successor(self, node_data):
		if self.root is None:
			print('Tree non-existent.\n')
			return None

		traversal_stack = Stack()
		traversal_node = self.root
		while traversal_node is not None or traversal_stack.is_empty() is False:
			while traversal_node is not None:
				traversal_stack.Push(traversal_node)
				traversal_node = traversal_node.get_left()

			traversal_node = traversal_stack.Pop()

			if traversal_node.get_data() == node_data:
                                if traversal_stack.is_empty() is False:
                                        successor_node = traversal_stack.get_top()
                                        print('Successor is : {}'.format(successor_node.get_data()))
                                        return successor_node
                                else:
                                        print('Inorder successor does not exist.\n')

			traversal_node = traversal_node.get_right()



def construct_incomplete_tree():
    binary_tree = BinaryTree(TreeNode(1))
    traversal_node = binary_tree.root

    traversal_node.set_left(TreeNode(2))
    traversal_node = traversal_node.get_left()

    traversal_node.set_left(TreeNode(3))
    traversal_node = traversal_node.get_left()

    traversal_node.set_left(TreeNode(4))
    traversal_node = traversal_node.get_left()

    traversal_node.set_right(TreeNode(5))

    traversal_node = binary_tree.fetch_tree_node(2)

    traversal_node.set_right(TreeNode(6))
    traversal_node = traversal_node.get_right()

    traversal_node.set_left(TreeNode(7))

    traversal_node.set_right(TreeNode(8))
    traversal_node = traversal_node.get_right()

    traversal_node.set_left(TreeNode(9))

    return binary_tree


def populate_inorder_traversal_queue(binary_tree):
	root = binary_tree.root
	if root is None:
		print('Tree non-existent.\n')
		return

	inorder_queue = Queue()
	populate_inorder_traversal_queue_util(root, inorder_queue)
	return inorder_queue


def populate_inorder_traversal_queue_util(node, inorder_queue):
	if node is None:
		return

	populate_inorder_traversal_queue_util(node.get_left(), inorder_queue)
	inorder_queue.Enqueue(node)
	populate_inorder_traversal_queue_util(node.get_right(), inorder_queue)


def construct_threaded_binary_tree_util(node, inorder_queue):
	if node is None:
		return

	if node.get_left() is not None:
		construct_threaded_binary_tree_util(node.get_left(), inorder_queue)

	inorder_queue.Dequeue()

	if node.get_right() is not None:
		construct_threaded_binary_tree_util(node.get_right(), inorder_queue)
	else:
		if inorder_queue.is_empty() is False:
			print('Threaded...\n')
			node.set_right(inorder_queue.get_front())
			node.set_right_thread_status(True)


def construct_threaded_binary_tree(binary_tree):
	root = binary_tree.root
	if root is None:
		print('Tree non-existent.\n')
		return

	inorder_queue = populate_inorder_traversal_queue(binary_tree)
	construct_threaded_binary_tree_util(root, inorder_queue)



if __name__ == "__main__":
    arr = list(range(1, 12))
    # random.shuffle(arr)

    # print(arr)

    # print("Converting to a complete binary tree...\n\n")

    # binary_tree = BinaryTree()
    # for i in arr:
    # 	binary_tree.insert_node(i)

    binary_tree = construct_incomplete_tree()

    print("Level Order Traversal :")
    binary_tree.level_order_traversal()

    print("\n\nInOrder Traversal(Recursive) :")
    binary_tree.inorder_traversal_recursive()


    # node_data = 0
    # while node_data != -1:
    #     node_data = int(input("\n\nFind Inorder Predecessor & Successor for : "))
    #     binary_tree.inorder_predecessor(node_data)
    #     binary_tree.inorder_successor(node_data)


    threaded_binary_tree = copy.deepcopy(binary_tree)
    print('Converting binary tree to right threaded binary tree...\n')
    construct_threaded_binary_tree(threaded_binary_tree)

    print('Checking threaded binary tree..\n')
    print('UN-THREADED :\n')
    traversal_node = binary_tree.fetch_tree_node(2)
    binary_tree.inorder_successor(traversal_node.get_data())

    print('THREADED :\n')
    traversal_node = threaded_binary_tree.fetch_tree_node(2)
    threaded_binary_tree.inorder_successor(traversal_node.get_data())