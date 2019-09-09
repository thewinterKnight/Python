# How do you find the middle element of a singly linked list in one pass? 


class Node(object):

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_next):
		self.next = new_next


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


def fetch_mid(head):
	slow_ptr = head.get_next()
	fast_ptr = head.get_next()

	while fast_ptr.get_next() and fast_ptr.get_next().get_next() is not None:
		fast_ptr = fast_ptr.get_next().get_next()
		slow_ptr = slow_ptr.get_next()

	return slow_ptr.get_data()


if __name__ == "__main__":
	linked_list = LinkedList()

	linked_list.insert_node(5)
	linked_list.insert_node(10)
	linked_list.insert_node(15)
	linked_list.insert_node(20)
	linked_list.insert_node(25)
	linked_list.insert_node(30)
	linked_list.insert_node(35)
	linked_list.insert_node(40)
	linked_list.insert_node(45)

	linked_list.print_linked_list()

	mid = fetch_mid(linked_list.head)
	print("Middle element of linked list : ", mid)
