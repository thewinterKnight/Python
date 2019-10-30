
class LinkedListNode:

	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_next(self, new_node):
		self.next = new_node


class Stack(LinkedListNode):

	def __init__(self, data=None):
		if data is not None:
			self.top = LinkedListNode(data)
		else:
			self.top = None

	def push(self, data):
		push_node = LinkedListNode(data)

		if self.top is None:
			self.top = push_node
		else:
			push_node.set_next(self.top)
			self.top = push_node

	def pop(self):
		if self.top is None:
			return None

		pop_node = self.top
		self.top = self.top.get_next()

		return pop_node.get_data()

	def get_front(self):
		return self.top.get_data()

	def is_empty(self):
		if self.top is None:
			return True
		return False


def compute_stock_span(arr):
	stock_stack = Stack(0)
	stock_spans = [1]

	for subindex, price in enumerate(arr[1:]):
		index = subindex + 1

		while stock_stack.is_empty() is False and arr[stock_stack.get_front()] <= price:
			stock_stack.pop()

		if stock_stack.is_empty() is True:
			stock_spans.append(index + 1)
		else:
			stock_spans.append(index - stock_stack.get_front())

		stock_stack.push(index)

	return stock_spans


def main():
	stock_prices = [100, 80, 60, 70, 60, 75, 85]
	# stock_prices = [10, 4, 5, 90, 120, 80]
	print(compute_stock_span(stock_prices))


if __name__=='__main__':
	main()