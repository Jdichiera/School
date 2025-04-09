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