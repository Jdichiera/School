from NumberList import NumberList
from NumberListNode import NumberListNode

class SortedNumberList(NumberList):
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        # TODO: Type your code here
        new_node = NumberListNode(number)
        
        if self.head is None:
            ''' if the head is null then the 
                incoming node will be the new head
                you just have to update the head and tail to point
                to the new node
            '''
            self.head = new_node
            self.tail = new_node
            return

        if number < self.get_head().get_data():
            ''' If the number is less than the new node is the new head
                store the existing head
                Update the new nodes next to the old head
                update the old heads prev to the new node
                update the head to be the new node
                '''
            old_head = self.get_head()
            new_node.set_next(old_head)
            old_head.set_previous(new_node)
            self.head = new_node
            return
        
        if number > self.tail.get_data():
            ''' if the number is greater than the tail 
                the new node is the new tail
                store the old tail
                update the new nodes previous to the old tail
                update the old tail next to new node
                update the tail to the new node
            '''
            old_tail = self.tail
            new_node.set_previous(old_tail)
            old_tail.set_next(new_node)
            self.tail = new_node
            return
        
        current_node = self.get_head()
        while current_node != None:
            if current_node.get_data() > number:
                ''' if the current node is greater than the number
                    the new node goes before the current node
                    update the new node next to the current node
                    update the new node prev to the current_node prev
                    update the current nodes previous to the new node
                    update the current node prev to the new node
                '''
                new_node.set_next(current_node)
                new_node.set_previous(current_node.get_previous())
                current_node.get_previous().set_next(new_node)
                current_node.set_previous(new_node)
                return
            current_node = current_node.get_next()
    
    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        ''' while the current node is not null
            if the current node is == number 
            
            if current node is head
            update head to current_node.next
            update new head's previous to None
            return true
            
            if the current node is the tail
            update tail to current_node.previous
            update new tail's next to None
            return true

            else the current node must be in the list
            update the current_node.previous.next to current_node.next
            update the current_node.next.previous to current_node.previous
            return true

            current_node = current_node.get_next()
        '''
        current_node = self.get_head()

        while current_node != None:
            if current_node.get_data() == number:                
                if current_node == self.head:
                    self.head = current_node.get_next()
                    if self.head:  # If list not empty after removal
                        self.head.set_previous(None)
                    else:  # If list now empty
                        self.tail = None
                    return True
                elif current_node == self.tail:
                    self.tail = current_node.get_previous()
                    self.tail.set_next(None)
                    return True
                else:
                    current_node.get_previous().set_next(current_node.get_next())
                    current_node.get_next().set_previous(current_node.get_previous())
                    return True
            
            current_node = current_node.get_next()
        return False