from linked_list import LinkedList
from node import Node

num_list = LinkedList() 
node_a = Node(54)
node_b = Node(2)
node_c = Node(72)
node_d = Node(36)

num_list.append(node_a)
num_list.append(node_b)
num_list.append(node_c)
num_list.append(node_d)

# Output list
print('List after adding nodes:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()

num_list.insertion_sort_singly_linked()

# Output list
print('List after insertion sort:', end=' ')
node = num_list.head
while node != None:
    print(node.data, end=' ')
    node = node.next
print()
