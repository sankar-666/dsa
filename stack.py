class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack Underflow")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack Underflow")

    def size(self):
        return len(self.items)
    
    def display(self):
        print(self.items)

# Example usage:
stack = Stack()

print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()

