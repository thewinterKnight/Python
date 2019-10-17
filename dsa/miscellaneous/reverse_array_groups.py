

class LinkedListNode:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_node):
		self.next = new_node


class Stack(LinkedListNode):

	def __init__(self, top=None):
		self.top = top

	def Push(self, new_data):
		new_node = LinkedListNode(new_data)

		if self.top is None:
			self.top = new_node
		else:
			new_node.set_next(self.top)
			self.top = new_node

	def Pop(self):
		if self.top is None:
			print('Stack non-existent.\n')
			return

		pop_node = self.top
		self.top = self.top.get_next()
		return pop_node.get_data()

	def is_empty(self):
		if self.top is None:
			return True
		return False

	def get_top(self):
		if self.top is None:
			return
		return self.top.get_data()


def reverse_array_groups(arr, width):
	reversal_stack = Stack()

	index = 0
	for item in arr:
		if index == width:
			while reversal_stack.is_empty() is False:
				print(reversal_stack.Pop())
			index = 0
		reversal_stack.Push(item)
		index += 1

	while reversal_stack.is_empty() is False:
		print(reversal_stack.Pop())


def main():
	# print('\nNumber of elements : ')
	# N = int(input())

	# arr = []
	# for i in range(0, N):
	# 	print('Enter element {}'.format(i+1))
	# 	arr.append(int(input()))

	# print('\nEnter reversal group size : ')
	# k = int(input())

	# arr = [10, 20, 30, 40, 50, 60]
	# k = 2

	arr = [1, 3, 6, 5, 7, 2]
	k = 3

	print('\nReversed grouped array :')
	reverse_array_groups(arr, k)


if __name__=="__main__":
	main()