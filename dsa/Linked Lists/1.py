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
	head = None

	def __init__(self, data=None, next=None):
		self.head = Node(data, next)

	def insert_node(self, data):
		new_node = Node(data)
		node = self.head
		while node.next != None:
			node = node.next

		node.set_next(new_node)

	def print_linked_list(self):
		node = self.head
		while node != None:
			print(node.data)
			node = node.next		


def fetch_mid(head):
	slow_ptr = head
	fast_ptr = head

	while fast_ptr.get_next() and fast_ptr.get_next().get_next() is not None:
		fast_ptr = fast_ptr.get_next().get_next()
		slow_ptr = slow_ptr.get_next()

	return slow_ptr.get_data()


if __name__ == "__main__":
	linked_list = LinkedList(1)

	linked_list.insert_node(5)
	linked_list.insert_node(10)
	linked_list.insert_node(15)
	linked_list.insert_node(20)
	linked_list.insert_node(25)
	linked_list.insert_node(30)
	linked_list.insert_node(35)
	linked_list.insert_node(40)
	linked_list.insert_node(45)
	linked_list.insert_node(50)
	linked_list.insert_node(55)
	linked_list.insert_node(60)
	linked_list.insert_node(70)
	linked_list.insert_node(80)

	linked_list.print_linked_list()

	mid = fetch_mid(linked_list.head)
	print("Middle element of linked list : ", mid)
