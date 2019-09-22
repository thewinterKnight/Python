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
            print("Queue non-existent.\n")
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
            print("Stack non-existent.\n")
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

    def set_left(self, new_tree_node):
        self.left = new_tree_node

    def set_right(self, new_tree_node):
        self.right = new_tree_node


class BinaryTree(TreeNode):
    insertion_queue = Queue()

    def __init__(self, root=None):
        self.root = root

    def fetch_tree_node(self, data_node):
        if self.root.get_data() == data_node:
            return self.root

        traversal_stack = Stack()
        traversal_node = self.root
        while traversal_stack.is_empty() is False or traversal_node is not None:
            while traversal_node is not None:
                traversal_stack.Push(traversal_node)
                traversal_node = traversal_node.get_left()

            traversal_node = traversal_stack.Pop()
            if traversal_node.get_data() == data_node:
                return traversal_node
            traversal_node = traversal_node.get_right()

    def insert_node(self, data):
        tree_node = TreeNode(data)

        if self.root is None:
            self.root = tree_node
        else:
            front = self.insertion_queue.get_front()

            if front.get_left() is None:
                front.set_left(tree_node)
            elif front.get_right() is None:
                front.set_right(tree_node)

            if front.get_left() is not None and front.get_right() is not None:
                self.insertion_queue.Dequeue()

        self.insertion_queue.Enqueue(tree_node)

    def level_order_traversal(self):
        if self.root is None:
            print("Tree non-existent.\n")
            return

        traversal_queue = Queue()
        traversal_queue.Enqueue(self.root)

        while traversal_queue.is_empty() is False:
            tree_node = traversal_queue.Dequeue()

            print(tree_node.get_data())

            if tree_node.get_left() is not None:
                traversal_queue.Enqueue(tree_node.get_left())
            if tree_node.get_right() is not None:
                traversal_queue.Enqueue(tree_node.get_right())

    def depth_traversals_recursive(self, type):
        if self.root is None:
            print("Tree non-existent.\n")
            return

        switcher = {
            "preorder": 0,
            "postorder": 2
        }

        self.depth_recursive_util(self.root, switcher.get(type, 1))

    def depth_recursive_util(self, node, print_index):
        if node is None:
            return

        left_flag = False
        for i in range(0, 3):
            if i == print_index:
                print(node.get_data())
            else:
                if left_flag is False:
                    self.depth_recursive_util(node.get_left(), print_index)
                    left_flag = True
                else:
                    self.depth_recursive_util(node.get_right(), print_index)

    def preorder_traversal_iterative(self):
        if self.root is None:
            print("Tree non-existent.\n")
            return

        traversal_stack = Stack()
        traversal_stack.Push(self.root)

        while traversal_stack.is_empty() is False:
            tree_node = traversal_stack.Pop()

            print(tree_node.get_data())
            if tree_node.get_right() is not None:
                traversal_stack.Push(tree_node.get_right())
            if tree_node.get_left() is not None:
                traversal_stack.Push(tree_node.get_left())

    def inorder_traversal_iterative(self):
        if self.root is None:
            print("Tree non-existent.\n")
            return

        traversal_stack = Stack()
        traversal_node = self.root
        while traversal_stack.is_empty() is False or traversal_node is not None:
            while traversal_node is not None:
                traversal_stack.Push(traversal_node)
                traversal_node = traversal_node.get_left()

            traversal_node = traversal_stack.Pop()
            print(traversal_node.get_data())
            traversal_node = traversal_node.get_right()

    def inorder_predecessor_util(self, traversal_node):
        if traversal_node is None:
            return None

        if traversal_node.get_right() is not None:
            while traversal_node.get_right() is not None:
                traversal_node = traversal_node.get_right()
            return traversal_node

        self.inorder_predecessor_util(traversal_node.get_left())

    def get_inorder_predecessor(self, data_node):
        node = self.fetch_tree_node(data_node)
        if node.get_left() is None:
            return node

        predecessor = self.inorder_predecessor_util(node.get_left())
        return predecessor


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


if __name__ == "__main__":
    arr = list(range(1, 12))
    # random.shuffle(arr)

    print(arr)

    print("Converting to a complete binary tree...\n\n")

    # binary_tree = BinaryTree()
    # for i in arr:
    # 	binary_tree.insert_node(i)

    binary_tree = construct_incomplete_tree()

    print("Level Order Traversal :")
    binary_tree.level_order_traversal()

    print("\n\nInOrder Traversal(Recursive) :")
    binary_tree.depth_traversals_recursive("inorder")

    print("\n\nInOrder Traversal(Iterative) :")
    binary_tree.inorder_traversal_iterative()

    print("\n\nPreOrder Traversal(Recursive) :")
    binary_tree.depth_traversals_recursive("preorder")

    print("\n\nPreOrder Traversal(Iterative) :")
    binary_tree.preorder_traversal_iterative()

    print("\n\nPostOrder Traversal(Recursive) :")
    binary_tree.depth_traversals_recursive("postorder")

    data_node = int(input("\n\nNode for inorder predecessor : "))
    inorder_predecessor = binary_tree.get_inorder_predecessor(data_node)
    print("The inorder predecessor of {} is {}".format(data_node, inorder_predecessor.get_data()))
