import random


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

        if self.top is not None:
            stack_node.set_next(self.top)
        self.top = stack_node

    def Pop(self):
        if self.top is None:
            print('Nothing to pop!!!\n')
            return None

        pop_node = self.top
        self.top = self.top.get_next()
        return pop_node.get_tree_node()

    def get_top(self):
        return self.head.get_tree_node()

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

    def set_left(self, new_left_node):
        self.left = new_left_node

    def set_right(self, new_right_node):
        self.right = new_right_node


class BinaryTree(TreeNode):

    def __init__(self, root=None):
        self.root = root

    def level_order_traversal(self):
        if self.root is None:
            print("Tree non-existent!!\n")
            return

        traversal_queue = Queue()
        traversal_queue.Enqueue(self.root)

        while traversal_queue.is_empty() is False:
            front_tree_node = traversal_queue.Dequeue()

            print(front_tree_node.get_data())

            if front_tree_node.get_left() is not None:
                traversal_queue.Enqueue(front_tree_node.get_left())
            if front_tree_node.get_right() is not None:
                traversal_queue.Enqueue(front_tree_node.get_right())


def insert_tree_node(binary_tree, data, insertion_queue):
    new_tree_node = TreeNode(data)

    if binary_tree.root is None:
        binary_tree.root = new_tree_node
    else:
        front_tree_node = insertion_queue.get_front()

        if front_tree_node.get_left() is None:
            front_tree_node.set_left(new_tree_node)
        elif front_tree_node.get_right() is None:
            front_tree_node.set_right(new_tree_node)

        if front_tree_node.get_left() is not None and front_tree_node.get_right() is not None:
            insertion_queue.Dequeue()

    insertion_queue.Enqueue(new_tree_node)


if __name__ == "__main__":
    binary_tree = BinaryTree()
    queue = Queue()

    arr = list(range(1, 12))
    random.shuffle(arr)

    print(arr)

    print("Converting to a complete binary tree...\n\n")

    for i in arr:
        insert_tree_node(binary_tree, i, queue)

    print("Level Order Traversal :")
    binary_tree.level_order_traversal()
