# How do you check if a given linked list contains a cycle? How do you find the starting node of the cycle?


class Node:

	def __init__ (self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_node):
		self.next = new_node

	def get_node(self, index):
		i = 0
		ptr = self.head
		while i < index:
			try:
				ptr = ptr.get_next()
			except ValueError:
				print("No node at index {}".format(index))
				return None
			i+=1
		return ptr


class LinkedList(Node):
	head = None

	def __init__(self, data=None, next=None):
		self.head = Node(data, next)

	def insert_node(self, data):
		new_node = Node(data)

		ptr = self.head
		while ptr.get_next() is not None:
			ptr = ptr.get_next()
		ptr.set_next(new_node)

	def print_linked_list(self):
		ptr = self.head
		while ptr is not None:
			print(ptr.get_data())
			ptr = ptr.get_next()
		print('\n')

	def get_last_node(self):
		ptr = self.head
		while ptr.get_next() is not None:
			ptr = ptr.get_next()
		return ptr


def detect_loop(head):
	fast_ptr = head
	slow_ptr = head

	while fast_ptr.get_next() and fast_ptr.get_next().get_next() is not None:
		fast_ptr = fast_ptr.get_next().get_next()
		slow_ptr = slow_ptr.get_next()

		if slow_ptr is fast_ptr:
			print("Loop detected in linked list!!!")
			return True, fast_ptr

	print("No loop in linked list")
	return False, None


def find_loop_node(head, fast_ptr):
	slow_ptr = head

	while slow_ptr is not fast_ptr:
		slow_ptr = slow_ptr.get_next()
		fast_ptr = fast_ptr.get_next()

	print("Loop occurs at {}".format(slow_ptr.get_data()))


def set_loop(linklist, loop_node_index):
	last_node = linklist.get_last_node()
	loop_node = linklist.get_node(loop_node_index)
	last_node.set_next(loop_node)


if __name__ is "__main__":
	linked_list = LinkedList(1)

	linked_list.insert_node(5)
	linked_list.insert_node(10)
	linked_list.insert_node(15)
	linked_list.insert_node(20)
	linked_list.insert_node(25)
	linked_list.insert_node(30)
	linked_list.insert_node(35)
	linked_list.insert_node(40)

	linked_list.print_linked_list()

	set_loop(linked_list, 5)

	is_loop, fast_ptr = detect_loop(linked_list.head)

	if is_loop:
		find_loop_node(linked_list.head, fast_ptr)
