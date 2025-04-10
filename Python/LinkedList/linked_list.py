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
            self.tail = new_node

    def prepend(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, current_node, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        elif current_node is self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = current_node.next
            current_node.next = new_node

    def remove_after(self, current_node):
        # if the current node is null but there is a head, then we are removing the first node
        # set the incoming node to the heads nextnode
        # if the incming node is also null then we know that we have removed the only node and
        # we can set the tail to none as well
        if (current_node == None) and (self.head != None):
            succeeding_node = self.head.next
            self_head = succeeding_node
            if succeeding_node == None:
                self.tail = None
        # If the current node is not null then it must be a node in the list
        # We want to set the incoming node to the current nodes next next - so two nodes ahead
        # this is because we will be removing the node after the current node
        # if the incoming node is null then that means the node we are removing is the tail
        # and we need to set the tail to the current node
        elif current_node != None:
            succeeding_node = current_node.next.next
            current_node.next = succeeding_node
            if succeeding_node == None:
                self.tail = current_node

    def insertion_sort_singly_linked(self):
        # we start two nodes into the list
        before_current = self.head
        current_node = before_current.next

        # while the current_node is not null
        # look for an insertion point where the current nodes data is less than the next node
        while current_node != None:
            next_node = current_node.next
            position = self.find_insertion_position(current_node.data)

            # If the position is the head of the list, then prepend the node to the head
            if position == before_current:
                before_current = current_node
            # If it isnt the head then we want to remove the node so we can insert it where 
            # it is less than the node after it
            else:
                self.remove_after(before_current)
                if position == None:
                    self.prepend(current_node)
                else:
                    self.insert_after(position, current_node)
            current_node = next_node

    def find_insertion_position(self, data_value):
        position_a = None
        position_b = self.head
        while (position_b != None and position_b.data < data_value):
            position_a = position_b
            position_b = position_b.next
        return position_a

