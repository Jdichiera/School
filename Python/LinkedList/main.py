from node import Node
from linked_list import Linked_List

def main():
    node1 = Node(25)
    node1.print_data()
    node2 = Node(50)
    node2.print_data()
    node1.next = node2
    node1.print_next()
    node2.print_next()


if __name__ == "__main__":
    main()