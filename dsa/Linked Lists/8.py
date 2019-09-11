# How do you find the sum of two linked lists using Stack? 

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

    def reverse_print_linked_list(self):
        self.reverse_print_util(self.head)

    def reverse_print_util(self, ptr):
        if ptr is None:
            return
        else:
            self.reverse_print_util(ptr.get_next())
            print(ptr.get_data())

    def get_length(self):
        if self.head is None:
            return 0

        i = 0
        ptr = self.head
        while ptr is not None:
            i += 1
            ptr = ptr.get_next()

        return i


def get_truncated_list(linked_list, truncate_node):
    if linked_list.head is None:
        return None

    ptr = linked_list.head
    while ptr.get_next() is not truncate_node:
        ptr = ptr.get_next()
    ptr.set_next(None)

    return LinkedList(linked_list.head)


def generate_equal_list(list_long, diff):
    i = 0
    equal_list_ptr = list_long.head
    while i < diff:
        equal_list_ptr = equal_list_ptr.get_next()
        i += 1

    return LinkedList(equal_list_ptr), equal_list_ptr


def insert_leftover_carry(carry):
    while carry / 10 != 0:
        sum_linked_list.insert_node(carry % 10)
        carry = int(carry / 10)


def insert_leftover_operand(ptr, carry):
    if ptr is None:
        return 0, carry

    _, prev_carry = insert_leftover_operand(ptr.get_next(), carry)

    sum = ptr.get_data() + prev_carry
    digit_sum = sum % 10
    digit_carry = int(sum / 10)

    global sum_linked_list
    sum_linked_list.insert_node(digit_sum)

    return digit_sum, digit_carry


def recursive_elementwise_sum(list1, list2):
    len1 = list1.get_length()
    len2 = list2.get_length()

    if len1 > len2:
        equal_list1, equal_list_ptr1 = generate_equal_list(list1, len1 - len2)
        _, carry = recursion_util(equal_list1.head, list2.head)
        overflow_list = get_truncated_list(list1, equal_list_ptr1)
        _, carry = insert_leftover_operand(overflow_list.head, carry)
    elif len1 < len2:
        equal_list2, equal_list_ptr2 = generate_equal_list(list2, len2 - len1)
        _, carry = recursion_util(list1.head, equal_list2.head)
        overflow_list = get_truncated_list(list2, equal_list_ptr2)
        _, carry = insert_leftover_operand(overflow_list.head, carry)
    else:
        _, carry = recursion_util(list1.head, list2.head)

    insert_leftover_carry(carry)


def recursion_util(ptr1, ptr2):
    if ptr1 is None:  # ...or if ptr2 is None
        return 0, 0

    _, prev_carry = recursion_util(ptr1.get_next(), ptr2.get_next())

    sum = ptr1.get_data() + ptr2.get_data() + prev_carry
    digit_sum = sum % 10
    digit_carry = int(sum / 10)

    global sum_linked_list
    sum_linked_list.insert_node(digit_sum)

    return digit_sum, digit_carry


if __name__ == "__main__":
    list1 = LinkedList()
    list2 = LinkedList()

    list1.insert_node(9)
    list1.insert_node(9)
    list1.insert_node(9)

    list2.insert_node(1)
    list2.insert_node(8)

    print('Linked list 1 -->\n')
    list1.print_linked_list()

    print('\n\nLinked list 2 -->\n')
    list2.print_linked_list()

    sum_linked_list = LinkedList()

    recursive_elementwise_sum(list1, list2)

    print('Sum linked list :\n')
    sum_linked_list.reverse_print_linked_list()
