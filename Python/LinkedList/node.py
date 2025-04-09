class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def print_data(self):
        print(self.data)

    def print_next(self):
        if self.next == None:
            print('No next node')
        else:
            self.next.print_data()