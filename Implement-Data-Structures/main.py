# main.py
from data_structures.linked_list import LinkedList
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.binary_tree import BinaryTree
from data_structures.other_data_structures import Set, Dictionary

# Testing the implemented data structures
if __name__ == "__main__":
    # Test linked list
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Test stack
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Test queue
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    # Test binary tree
    binary_tree = BinaryTree()
    binary_tree.insert(5)
    binary_tree.insert(7)

    # Test set
    my_set = Set()
    my_set.add(1)
    my_set.add(2)
    my_set.add(3)
    print(my_set.contains(2))  # True
    print(my_set.size())        # 3

    # Test dictionary
    my_dict = Dictionary()
    my_dict.add('a', 1)
    my_dict.add('b', 2)
    my_dict.add('c', 3)
    print(my_dict.get('b'))     # 2
    print(my_dict.size())       # 3
