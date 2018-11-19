class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []


stack = Stack()

reverse = ""

for i in "yesterday":
    stack.push(i)

print(stack.items)

for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
