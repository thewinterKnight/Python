# How do you reverse a linked list using recursion?


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
			new_node = Node(data)
			ptr = self.head
			while ptr.get_next() is not None:
				ptr = ptr.get_next()
			ptr.set_next(new_node)

	def print_linked_list(self):
		if self.head is None:
			print("Nothing to print\n")
			return
		ptr = self.head
		while ptr is not None:
			print(ptr.get_data())
			ptr = ptr.get_next()


def reverse_linked_list(ptr):
	if ptr.get_next() is None:
		global head
		head = ptr
		return head

	reverse_linked_list(ptr.get_next())

	temp = ptr.get_next()
	temp.set_next(ptr)
	ptr.set_next(None)


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
	reverse_linked_list(linked_list.head)
	linked_list = LinkedList(head)

	linked_list.print_linked_list()
