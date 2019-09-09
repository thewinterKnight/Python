# How do you reverse a singly linked list without recursion?

import copy


class Node:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_node):
		self.next = new_node


class LinkedList(Node):

	def __init__(self, head=None):
		self.head = head

	def insert_node(self, data):
		if self.head is None:
			self.head = Node(data)
		else:
			ptr = self.head
			while ptr.get_next() is not None:
				ptr = ptr.get_next()
			ptr.set_next(Node(data))

	def print_linked_list(self):
		if self.head is None:
			print("Nothing to print\n")
			return

		ptr = self.head
		while ptr is not None:
			print(ptr.get_data())
			ptr = ptr.get_next()


def reverse_linked_list(ptr):
	ptr1 = ptr.get_next()
	ptr2 = ptr1.get_next()

	ptr.set_next(None)
	while ptr2 is not None:
		ptr1.set_next(ptr)
		ptr = ptr1
		ptr1 = ptr2
		ptr2 = ptr2.get_next()
	ptr1.set_next(ptr)
	ptr = ptr1

	global reverse_head
	reverse_head = ptr


if __name__ is "__main__":
	linked_list = LinkedList()

	linked_list.insert_node(5)
	linked_list.insert_node(10)
	linked_list.insert_node(15)
	linked_list.insert_node(20)
	linked_list.insert_node(25)
	linked_list.insert_node(30)
	linked_list.insert_node(35)
	linked_list.insert_node(40)

	linked_list.print_linked_list()

	print("Reversing...\n")
	copy_linked_list = copy.deepcopy(linked_list)
	reverse_linked_list(copy_linked_list.head)

	reverse_linked_list = LinkedList(reverse_head)

	reverse_linked_list.print_linked_list()

	# print('\n\n')
	# linked_list.print_linked_list()

