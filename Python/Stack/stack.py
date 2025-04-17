class Stack:
    def __init__(self, optional_max_length = -1):
        self.stack_list = []
        self.max_length = optional_max_length

    def __len__(self):
        return len(self.stack_list)

    def pop(self):
        return self.stack_list.pop()
    
    def push(self, item):
        if len(self.stack_list) == self.max_length:
            return False
        
        self.stack_list.append(item)
        return False