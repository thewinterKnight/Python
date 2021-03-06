# How do you find the length of a singly linked list using recursion?

import random
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
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
		else:
			ptr = self.head
			while ptr.get_next() is not None:
				ptr = ptr.get_next()
			ptr.set_next(new_node)

	def print_linked_list(self):
		if self.head is None:
			print("Nothing to print\n")
		else:
			ptr = self.head
			while ptr is not None:
				print(ptr.get_data())
				ptr = ptr.get_next()

	def delete_node(self, node):
		ptr = self.head
		while ptr.get_next() is not node:
			ptr = ptr.get_next()
		ptr.set_next(ptr.get_next().get_next())
		del(node)

		return ptr 


def create_linked_list(min_value, max_value, num_unique_elements, num_duplicates):
	assert num_duplicates < int(num_unique_elements/2)

	num_list = []
	i=0
	while i < num_unique_elements:
		num_list.append(random.randint(min_value, max_value))
		i += 1

	duplication_indices = list(range(0, num_unique_elements-1))
	random.shuffle(duplication_indices)
	duplication_indices = duplication_indices[:num_duplicates]

	duplicate_list = list(map(lambda indx : num_list[indx], duplication_indices))

	num_list.extend(duplicate_list)
	random.shuffle(num_list)

	linked_list = LinkedList()
	for num in num_list:
		linked_list.insert_node(num)

	return linked_list


def third_node_from_end(ptr, index_from_end=None):
	global node_from_end
	if ptr is None:
		return 0

	reverse_indx = 1 + third_node_from_end(ptr.get_next(), index_from_end)

	if reverse_indx == index_from_end:
		node_from_end = ptr
	return reverse_indx


if __name__=="__main__":
	m = 3
	M = 9
	total_elements = 7
	dups = 1
	linked_list = create_linked_list(min_value=m, max_value=M, num_unique_elements=total_elements-dups, num_duplicates=dups)

	linked_list.print_linked_list()

	indx = 3
	third_node_from_end(linked_list.head, index_from_end=indx)

	print('\n\n{} node from end of linked list is {}'.format(indx, node_from_end.get_data()))

