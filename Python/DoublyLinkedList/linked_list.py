class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node == self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            successor_node = current_node.next
            new_node.next = successor_node
            new_node.prev = current_node
            current_node.next = new_node
            successor_node.prev = new_node

    def remove(self, current_node):
        successor_node = current_node.next
        predesessor_node = current_node.prev

        if successor_node is not None:
            successor_node.prev = predesessor_node
        
        if predesessor_node is not None:
            predesessor_node.next = successor_node

        if current_node is self.head:
            self.head = successor_node

        if current_node is self.tail:
            self.tail = predesessor_node

    def insertion_sort_doubly_linked(self):
        # Start at the second node in. 
        current_node = self.head.next

        # While the current node is not null we want to step through these steps
        # set the next node to the node ahead of the current node
        # set the search node to the node behind the current node
        while current_node != None:
            next_node = current_node.next
            search_node = current_node.prev
            # while the search nodes value is greater than the current node
            # keep sliding the search node back
            while (search_node != None and search_node.data > current_node.data):
                search_node = search_node.prev

            # once the search node has found a spot where it is less than the 
            # current_node. That is where we want to put the current node
            # remove the current node and put it back in the spot we found
            self.remove(current_node)

            # If the search node is null then we are at the head of the list
            if (search_node == None):
                current_node.prev = None
                self.prepend(current_node)
            else:
                self.insert_after(search_node, current_node)

            current_node = next_node
        
